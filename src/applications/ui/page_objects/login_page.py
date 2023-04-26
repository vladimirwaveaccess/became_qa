import time
from selenium.webdriver.common.by import By

from src.applications.ui.page_objects.forgot_password_page import ForgotPasswordPage
from src.applications.ui.page_objects.sign_up_page import SignUpPage
from src.config.config import CONFIG


class LoginPage:
    URL = "/login"

    USERNAME_FLD = (By.ID, "login_field")
    PASSWORD_FLD = (By.ID, "password")
    SIGN_IN_BTN = (By.NAME, "commit")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(),'Incorrect username or password.')]")
    FORGOT_PASSWORD = (By.XPATH, "//a[@href='/password_reset']")

    def __init__(self, app) -> None:
        self.app = app

    def go_to(self):
        self.app.go_to(CONFIG.get("BASE_URL_UI") + LoginPage.URL)

    def try_sign_in(self, username, password):
        self.app.type_text(LoginPage.USERNAME_FLD, username)
        self.app.type_text(LoginPage.PASSWORD_FLD, password)
        self.app.click(LoginPage.SIGN_IN_BTN)
        time.sleep(5)

        return self

    def open_sign_up_page(self):
        sing_up_page = SignUpPage(self.app)
        sing_up_page.wait_loaded()

        return sing_up_page

    def open_forgot_password_page(self):
        forgot_password_page = ForgotPasswordPage(self.app)
        forgot_password_page.wait_loaded()

        return forgot_password_page

    def click_to_forgot_pass_page(self):
        self.app.click(LoginPage.FORGOT_PASSWORD)

    def get_error_message(self):
        return self.app.get_text(LoginPage.ERROR_MESSAGE)
