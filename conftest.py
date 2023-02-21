import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://stellarburgers.nomoreparties.site/'
@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")
    #options.add_argument("--headless") #запуск теста без открытия браузера - иногда такое нужно

    browser_driver = webdriver.Chrome(options=options)
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()