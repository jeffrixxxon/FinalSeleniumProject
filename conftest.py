import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="See the required language in the format: --language=user_language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nstart {user_language} language for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': f'{user_language}'})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()