import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()
