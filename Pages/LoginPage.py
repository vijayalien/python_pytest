from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    element_email = (By.ID, "user-name")
    element_password = (By.ID, "password")
    element_login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    def get_login_page(self, title):
        self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.element_email, username)
        self.do_send_keys(self.element_password, password)
        self.do_click(self.element_login_button)
