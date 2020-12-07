import pytest

from api.api_client import ApiClient
from orm.orm_builder import MysqlOrmBuilder
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from strgen import StringGenerator


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request, mysqlconnection):
        self.driver = driver
        self.config = config
        self.mysql = mysqlconnection
        self.builder = MysqlOrmBuilder(connection=self.mysql)
        self.url = config["url"]
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.auth_page: AuthPage = request.getfixturevalue('auth_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.api_client: ApiClient = request.getfixturevalue('api_client')


def generate_user(len_user=8, len_pass=4, russian_username=False, russian_email=False, mask=True):
    username = StringGenerator("[a-z]{%d}" % len_user if not russian_username else "[а-я]{%d}" % len_user).render()
    if mask:
        email = StringGenerator("[a-z]{3:5}@[\c]{3:4}.(com|net|ru)").render()
    elif russian_email:
        email = StringGenerator('[а-я]{3:5}@[\c]{3:4}.(com|net|ru)').render()
    else:
        email = StringGenerator('[a-z]{10}').render()
    password = StringGenerator('[a-zZ-A0-9]{%d}' % len_pass).render()
    return username, email, password, password
