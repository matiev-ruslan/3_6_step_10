import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, es or other")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')

@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language_chrome = request.config.getoption('user_language_chrome')
    user_language_firefox = request.config.getoption('user_language_firefox')

    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_language': user_language_chrome})

    firefox_options = OptionsFirefox()
    firefox_options.set_preference('intl.accept_languages', user_language_firefox)

    if (browser_name == 'chrome'):
        print("\nStart Chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif (browser_name == 'firefox'):
        print("\nStart Firefox browser for test..")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        print("\nBrowser <browser_name> not implemented..")



    yield browser
    print("\nquit browser..")
    browser.quit()