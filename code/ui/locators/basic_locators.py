from selenium.webdriver.common.by import By


class BaseLocators:
    LOGIN_FIELD = (By.XPATH,  '//input[@name="username"]')
    PASSWD_FIELD = (By.XPATH, '//input[@name="password"]')

    AUTHORIZATION_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Login"]')

    INVALID_LOGIN_OR_PASSWD = (By.XPATH, '//div[text()="Invalid username or password"]')
    INVALID_USERNAME_LENGTH = (By.XPATH, '//div[text()="Incorrect username length"]')


class AuthLocators(BaseLocators):
    CREATE_ACCOUNT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Create an account')
    INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
    INPUT_REPEAT_PASSWORD = (By.XPATH, '//input[@name="confirm"]')
    ACCEPT_BUTTON = (By.XPATH, '//input[@name="term"]')
    REGISTER_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Register"]')

    #errors
    INVALID_EMAIL = (By.XPATH, '//div[text()="Invalid email address"]')
    INVALID_NAME = (By.XPATH, '//div[text()="Incorrect username length"]')
    INVALID_EXIST_EMAIL_SERVER_ERROR = (By.XPATH, '//div[text()="Internal Server Error"]')
    INVALID_PASSWORD_MATCH = (By.XPATH, '//div[text()="Passwords must match"]')
    INVALID_EXIST_USER = (By.XPATH, '//div[text()="User already exist"]')

    #logout
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')


class MainPageLocators(AuthLocators):
    API_LOCATOR = (By.XPATH, '//div//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    INTERNET_LOCATOR = (By.XPATH, '//div//a[@href="https://www.popularmechanics.com/technology/infrastructure'
                                  '/a29666802/future-of-the-internet/"]')
    SMTP_LOCATOR = (By.XPATH, '//div//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')
    PHRASE_LOCATOR = (By.XPATH, '//p[2]')
    PYTHON_LOCATOR = (By.XPATH, '//div//a[@href="https://www.python.org/"]')
    PYTHON_HISTORY = (By.XPATH, '//div//a[@href="https://en.wikipedia.org/wiki/History_of_Python"]')
    FLASK_LOCATOR = (By.XPATH, '//div//a[@href="https://flask.palletsprojects.com/en/1.1.x/#"]')
    LINUX_LOCATOR = (By.XPATH, '(//div//a[@href="javascript:"])[1]')
    NETWORK_LOCATOR = (By.XPATH, '(//div//a[@href="javascript:"])[2]')
    CENTOS_LOCATOR = (By.XPATH, '//div//a[@href="https://getfedora.org/ru/workstation/download/"]')
    NEWS_LOCATOR = (By.XPATH, '//div//a[@href="https://www.wireshark.org/news/"]')
    DOWNLOAD_LOCATOR = (By.XPATH, '//div//a[@href="https://www.wireshark.org/#download"]')
    EXAMPLES_LOCATOR = (By.XPATH, '//div//a[@href="https://hackertarget.com/tcpdump-examples/"]')


class CreateAdvert(AuthLocators):
    COMPANY_BUTTON = (By.XPATH, '//a[contains(@class, "center-module-campaigns")]')
    NEW_CAMPAIGN = (By.XPATH, ['//a[@href="/campaign/new" and contains(@class, "campaigns-tbl-settings")]',
                               '//div[contains(@class, "no-campaigns-msg")]//a'])
    AUDIO_ADVERT = (By.XPATH, '//div[contains(@class,"audiolistening")]')
    ADD_AUDIO = (By.XPATH, '//div[contains(@class,"input__file-wrap")]/input')
    ADD_ADVERT = (By.XPATH, '//div[contains(@class, "js-save-button-wrap")]/button')
    DONE = (By.XPATH, '//div[contains(@class, "icon-success")]')


class CreateSegment(AuthLocators):
    AUDITORY_BUTTON = (By.XPATH, '//a[@href="/segments"]')
    CREATE_SEGMENT = (
        By.XPATH, ['//a[@href="/segments/segments_list/new"]', '//button[contains(@class, "button button_submit")]'])
    ADD_SEGMENT = (By.XPATH, '//span[@data-translated="Add audience segments..."]')
    CHECKBOX = (By.XPATH, '//input[contains(@class, "source-checkbox")]')
    INPUT_NAME = (By.XPATH, '//div[@class="input input_create-segment-form"]//input[contains(@class, "input__inp")]')
    ADD_SEGMENT_FINAL = (By.XPATH, '//div[contains(@class, "js-add-button")]')
    DONE = (By.XPATH, '//div[contains(@class, "create-segment-form__btn-wrap")]/button')
    CHECK_IS_CREATED = (By.XPATH, '//table[contains(@class, "js-table")]')


class DeleteSegment(AuthLocators):
    DELETE_SEGMENT = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')
    CHECK_IS_CREATED = (By.XPATH, '//div[contains(@class, "js-modal-view-body")]')

    def detele_selected_segment(self, name):
        return By.XPATH, f'//a[contains(text(), "{name}")]//..//..//div[contains(@class, "remove-source-wrap")]'
