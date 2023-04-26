from src.applications.ui.base_app import BaseAPP
from src.applications.ui.page_objects.forgot_password_page import ForgotPasswordPage
from src.applications.ui.page_objects.login_page import LoginPage
from src.applications.ui.page_objects.sign_up_page import SignUpPage
from src.config.config import CONFIG



class GitHubUI(BaseAPP):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.LoginPage = LoginPage(self)
        self.SingUpPage = SignUpPage(self)
        self.SingUpPage = ForgotPasswordPage(self)

    def open(self):
        self.driver.get(CONFIG.get("BASE_URL_UI"))
        return self

    def quit(self):
        self.driver.quit()
