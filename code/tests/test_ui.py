import allure
import pytest
from tests.base import BaseCase, generate_user


@pytest.mark.UI
class TestReg(BaseCase):

    def test_reg_success(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        user = self.builder.get_access(username)
        assert user.username == username
        self.builder.del_user(username)

    def test_reg_exist_user(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.auth_page.logout()
        self.auth_page.registration(username, email, password, password2)
        assert "User already exist" in self.driver.page_source
        self.builder.del_user(username)

    def test_reg_incorrect_username_length_min(self):
        username, email, password, password2 = generate_user(len_user=5)
        self.auth_page.registration(username, email, password, password2)
        assert "Incorrect username length" in self.driver.page_source
        self.builder.del_user(username)

    def test_reg_incorrect_username_length_max(self):
        username, email, password, password2 = generate_user(len_user=17)
        self.auth_page.registration(username, email, password, password2)
        assert "Incorrect username length" in self.driver.page_source
        self.builder.del_user(username)

    def test_reg_repeat_password_negative(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, generate_user()[2], password2)
        assert "Passwords must match" in self.driver.page_source
        self.builder.del_user(username)

    def test_reg_invalid_email(self):
        username, email, password, password2 = generate_user(mask=False)
        self.auth_page.registration(username, email, password, password2)
        assert "Invalid email address" in self.driver.page_source
        self.builder.del_user(username)

    def test_reg_exist_email(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.auth_page.logout()
        self.auth_page.registration(generate_user()[0], email, password, password2)
        self.builder.del_user(username)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='test_python_link',
                      attachment_type=allure.attachment_type.PNG)
        assert "Email already exist" in self.driver.page_source

    def test_reg_several_incorrect_fields(self):
        username, email, password, password2 = generate_user(len_user=1, mask=False)
        self.auth_page.registration(username, email, password, generate_user()[2], password2)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='test_python_link',
                      attachment_type=allure.attachment_type.PNG)
        assert "Incorrect username length, incorrect email address, passwords must match" in self.driver.page_source


@pytest.mark.UI
class TestLogin(BaseCase):

    def test_login(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.auth_page.logout()
        self.auth_page.login(username, password)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source
        self.builder.del_user(username)

    def test_login_negative(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.auth_page.logout()
        self.auth_page.login(generate_user()[0], password)
        assert "Invalid username or password" in self.driver.page_source
        self.builder.del_user(username)


@pytest.mark.UI
class TestMainPage(BaseCase):
    def test_logout(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.auth_page.logout()
        assert "Welcome to the TEST SERVER" in self.driver.page_source
        self.builder.del_user(username)

    def test_logout_access_flag(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.auth_page.logout()
        result_flag = self.builder.get_access(username)
        assert result_flag == 0
        self.builder.del_user(username)

    def test_logged_as(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        assert f'Logged as {username}' in self.driver.page_source
        self.builder.del_user(username)

    def test_api_link(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.click(self.main_page.locators.API_LOCATOR)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert 'https://en.wikipedia.org/wiki/API' == self.driver.current_url

    def test_internet_future_link(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.click(self.main_page.locators.INTERNET_LOCATOR)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert "https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/" \
               == self.driver.current_url

    def test_smtp_link(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.click(self.main_page.locators.SMTP_LOCATOR)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.builder.del_user(username)
        assert "https://ru.wikipedia.org/wiki/SMTP" == self.driver.current_url

    def test_change_phrase(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        phrase = self.main_page.find(self.main_page.locators.PHRASE_LOCATOR).text
        self.driver.refresh()
        self.builder.del_user(username)
        assert phrase != self.main_page.find(self.main_page.locators.PHRASE_LOCATOR).text

    def test_python_link(self):
        username, email, password, password2 = generate_user() ####???
        self.auth_page.registration(username, email, password, password2)
        self.main_page.click(self.main_page.locators.PYTHON_LOCATOR)
        self.builder.del_user(username)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='test_python_link',
                      attachment_type=allure.attachment_type.PNG)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert "https://www.python.org/" == self.driver.current_url

    def test_python_history(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.move(self.main_page.locators.PYTHON_LOCATOR)
        self.main_page.click(self.main_page.locators.PYTHON_HISTORY)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert "https://en.wikipedia.org/wiki/History_of_Python" == self.driver.current_url

    def test_about_flask(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.move(self.main_page.locators.PYTHON_LOCATOR)
        self.main_page.click(self.main_page.locators.FLASK_LOCATOR)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert "https://flask.palletsprojects.com/en/1.1.x/#" == self.driver.current_url

    def test_centos(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.move(self.main_page.locators.LINUX_LOCATOR)
        self.main_page.click(self.main_page.locators.CENTOS_LOCATOR)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[1])
        allure.attach(body=self.driver.get_screenshot_as_png(),
                      name='test_python_link',
                      attachment_type=allure.attachment_type.PNG)
        assert "https://getfedora.org/ru/workstation/download/" == self.driver.current_url

    def test_wireshark_news(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.move(self.main_page.locators.NETWORK_LOCATOR)
        self.main_page.click(self.main_page.locators.NEWS_LOCATOR)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "https://www.wireshark.org/news/" == self.driver.current_url
        self.builder.del_user(username)

    def test_wireshark_download(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.move(self.main_page.locators.NETWORK_LOCATOR)
        self.main_page.click(self.main_page.locators.DOWNLOAD_LOCATOR)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "https://www.wireshark.org/#download" == self.driver.current_url

    def test_examples(self):
        username, email, password, password2 = generate_user()
        self.auth_page.registration(username, email, password, password2)
        self.main_page.move(self.main_page.locators.NETWORK_LOCATOR)
        self.main_page.click(self.main_page.locators.EXAMPLES_LOCATOR)
        self.builder.del_user(username)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "https://hackertarget.com/tcpdump-examples/" == self.driver.current_url
