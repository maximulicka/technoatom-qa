FROM python:3.8

COPY . /vk_mock
WORKDIR /vk_mock

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask_app.py"]