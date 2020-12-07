import pytest
import allure

from api.api_client import ApiClient
from tests.base import BaseCase


@pytest.mark.API
class TestApi(BaseCase):

    # @pytest.fixture(scope='function')
    # def api_client(self):
    #     username = 'maxroot'
    #     password = '123'
    #     email = 'max@yandex.ru'
    #     return ApiClient(username, password, email)

    def test_add_user_true(self, api_client):
        username = 'kolyan'
        result = api_client.reg_user(username, 'kolyan@yandex.ru', 'qwerty')
        assert result == 210
        self.builder.del_user(username)
