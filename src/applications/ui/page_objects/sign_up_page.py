from selenium.webdriver.common.by import By


class SignUpPage:
    IMG_AVATAR = (By.XPATH, "//img[@class='avatar avatar-small circle']")
    NAME_AVATAR = (By.XPATH, "//strong[@class='css-truncate-target']")

    def __init__(self, app) -> None:
        self.app = app

    def wait_loaded(self):
        self.app.wait_loaded(SignUpPage.IMG_AVATAR)

    def click_avatar(self):
        self.app.click(SignUpPage.IMG_AVATAR)

    def get_user_name(self):
        return self.app.get_text(SignUpPage.NAME_AVATAR)
