from ui.fixtures import *
from orm.orm_client import MysqlOrmConnection


def pytest_addoption(parser):
    parser.addoption('--url', default='http://myapp:5555')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='80.0')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='function')
def mysqlconnection():
    return MysqlOrmConnection(user='test_qa', password='qa_test', db_name="QA_DB", host="127.0.0.1", port=3306)

