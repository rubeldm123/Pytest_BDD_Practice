import pytest
from pytest_bdd import *
from selenium import webdriver
import time

from pages.HomePage import Homepage
from pages.LoginPage import LoginPage

url = 'https://opensource-demo.orangehrmlive.com/'
scenarios('../features/oranghrmscenario.feature')


@given("I launch browser")
def step_impl(driver):
    print("Browser open successfully")
    driver.get(url)


@when("Enter valid username and password")
def step_impl(driver):
    lp = LoginPage(driver)
    lp.enterUsrname().send_keys("Admin")
    lp.enterPassword().send_keys("admin123")
    print("Enter username and password successfully")


@when("click on login")
def step_impl(driver):
    lp = LoginPage(driver)
    lp.clickLoginBtn().click()
    print("Click on click button successfully")


@then("I should landed to the HomePage")
def step_impl(driver):
    hp = Homepage(driver)
    actual = 'Dashboardd'
    expected = hp.getDashboardtext().text
    if actual != expected:
        print("they are not Equal")
        driver.close()
