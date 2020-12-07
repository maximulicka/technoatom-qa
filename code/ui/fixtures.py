import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from api.api_client import ApiClient
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.auth_page import AuthPage


class UsupportedBrowserException(Exception):
    pass


# @pytest.fixture(scope='function')
# def del_user(request):
#     yield
#     def wrapper(username):
#         request.instance.builder.del_user(username)
#     return wrapper


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture(scope='function')
def api_client():
    username = 'maxroot'
    password = '123'
    email = 'max@yandex.ru'
    return ApiClient(username, password, email)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    #window_size = request.config.getoption('--window-size')
    return {'browser': browser,
            'version': version,
            'url': url,
            'download_dir': '/tmp',
            'selenoid': selenoid}
            #'window_size': window_size}


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']
    selenoid = config['selenoid']

    if browser == 'chrome':
        options = ChromeOptions()
        if selenoid:
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True, 'browserName': 'chrome'})

        else:
            options.add_argument("--window-size=800,600")

            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)

            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    # quit = закрыть страницу, остановить browser driver
    # close = закрыть страницу, бинарь browser driver останется запущенным
    driver.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver

    driver.quit()
