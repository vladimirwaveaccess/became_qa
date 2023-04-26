from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    NAME_OF_PAGE = (By.XPATH, "//h1[contains(text(), 'Reset your password')]")

    def __init__(self, app) -> None:
        self.app = app

    def wait_loaded(self):
        self.app.wait_loaded(ForgotPasswordPage.NAME_OF_PAGE)

    def get_title_page(self):
        return self.app.get_text(ForgotPasswordPage.NAME_OF_PAGE)
