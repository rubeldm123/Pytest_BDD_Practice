from pytest_bdd import scenarios, parsers, given, when, then
import pytest
from selenium import webdriver
import time

url = 'https://opensource-demo.orangehrmlive.com/'
# scenarios('C:/Users/rubel/Desktop/SeleniumWithPython/pytestBDDPractice/test/features/oranghrmscenario.feature')
scenarios('../features/orgparameters.feature')


@pytest.fixture()
def browser():
    # b = webdriver.Chrome(executable_path='C:/Users/rubel/Downloads/chromedriver_win32/chromedriver.exe')
    b = webdriver.Chrome(executable_path='C:/Users/rubel/Desktop/SeleniumWithPython/pytestBDDPractice/chromedriver.exe')
    b.implicitly_wait(10)
    yield b
    # b.quit()


@given("I launch ORG browser")
def step_impl(browser):
    browser.get(url)
    browser.implicitly_wait(10)
    print("Browser open successfully")


@when('Enter valid "<username>"')
def step_impl(browser, username):
    browser.find_element_by_xpath("//div[@id='divUsername']/input[@name='txtUsername']").send_keys(username)


@when('Enter valid "<password>"')
def step_impl(browser, password):
    browser.find_element_by_xpath("//div[@id='divPassword']/input[@name='txtPassword']").send_keys(password)


@when("click on Submit Button")
def step_impl(browser):
    browser.find_element_by_xpath("//div[@id='divLoginButton']/input[@name='Submit']").click()


@then("I should be landing in Homepage")
def step_impl(browser):
    hp = 'Dashboard'
    tag = browser.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    assert hp == tag
    print("Actual tag is ", tag)
