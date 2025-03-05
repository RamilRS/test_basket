import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def language(request):
    lng = request.config.getoption("language")
    if lng==None:
        lng="ru"
    return lng

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
