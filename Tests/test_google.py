from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_title_is_visible(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title("Google")
        assert title == "Google"