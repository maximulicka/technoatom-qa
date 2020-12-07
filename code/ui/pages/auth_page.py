from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class AuthPage(BasePage):
    locators = basic_locators.AuthLocators()

    def login(self, username, password):
        self.fill_field(self.locators.LOGIN_FIELD, username)
        self.fill_field(self.locators.PASSWD_FIELD, password)
        self.click(self.locators.AUTHORIZATION_BUTTON)

    def registration(self, username, email, password, password2, terms=True, ):
        self.click(self.locators.CREATE_ACCOUNT_BUTTON)
        self.fill_field(self.locators.LOGIN_FIELD, username)
        self.fill_field(self.locators.INPUT_EMAIL, email)
        self.fill_field(self.locators.PASSWD_FIELD, password)
        self.fill_field(self.locators.INPUT_REPEAT_PASSWORD, password2)
        if terms:
            self.click(self.locators.ACCEPT_BUTTON)
        self.click(self.locators.REGISTER_BUTTON)

    def logout(self, timeout=None):
        self.click(self.locators.LOGOUT_BUTTON, timeout)
