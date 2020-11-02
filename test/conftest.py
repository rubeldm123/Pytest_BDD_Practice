import pytest
from pytest_bdd import *
from selenium import webdriver
import time

# url = 'https://opensource-demo.orangehrmlive.com/'

# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        d = webdriver.Chrome(executable_path='C:/Users/rubel/Downloads/chromedriver_win32/chromedriver.exe')
        # b = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        # driver.get(url)
        d.maximize_window()
        d.implicitly_wait(10)
        return d
    # cmd command: pytest --browser_name chrome test_orgFirstTest.py -s -v


    else:
        print("driver not choose")
