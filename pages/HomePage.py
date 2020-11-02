from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    dashboard_text = (By.XPATH, "//h1[contains(text(),'Dashboard')]")

    def getDashboardtext(self):
        return self.driver.find_element(*Homepage.dashboard_text)
