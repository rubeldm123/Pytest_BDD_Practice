from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    userName = (By.XPATH, "//div[@id='divUsername']/input[@name='txtUsername']")
    password = (By.XPATH, "//div[@id='divPassword']/input[@name='txtPassword']")
    loginbtn = (By.XPATH, "//div[@id='divLoginButton']/input[@name='Submit']")

# driver.find_element_by_xpath("//div[@id='divUsername']/input[@name='txtUsername']").send_keys("Admin")
#     driver.find_element_by_xpath("//div[@id='divPassword']/input[@name='txtPassword']").send_keys("admin123")
#
# driver.find_element_by_xpath("//div[@id='divLoginButton']/input[@name='Submit']").click()

    def enterUsrname(self):
        return self.driver.find_element(*LoginPage.userName)

    def enterPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickLoginBtn(self):
        return self.driver.find_element(*LoginPage.loginbtn)