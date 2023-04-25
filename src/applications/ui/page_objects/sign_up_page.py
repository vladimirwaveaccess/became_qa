from selenium.webdriver.common.by import By


class SignUpPage:
    IMG_AVATAR = (By.XPATH, "//img[@class='avatar avatar-small circle']")

    def __init__(self, app) -> None:
        self.app = app

    def wait_loaded(self):
        self.app.wait_loaded(SignUpPage.IMG_AVATAR)
