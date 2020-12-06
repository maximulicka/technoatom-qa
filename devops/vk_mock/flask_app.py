import json

from flask import Flask, request
from threading import Thread

app = Flask(__name__)

users = {"testuser1": '123', 'testuser2': "321"}


def run_server():
    server = Thread(target=app.run, kwargs={'host': "vk_mock", 'port': "5556"})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


@app.route('/vk_id/<username>', methods=["GET", "POST"])
def index(username):
    if request.method == "GET":
        if users.get(username):
            return {"vk_id": users.get(username)}, 200
        return {}, 404
    elif request.method == "POST":
        users[username] = json.loads(request.data.decode()).get('vk_id')


if __name__ == '__main__':
    run_server()
