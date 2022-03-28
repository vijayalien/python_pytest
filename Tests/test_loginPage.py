from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_title_is_visible(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title("Swag Labs")
        assert title == "Swag Labs"

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("standard_user", "secret_sauce")
