from src.config.config import CONFIG
from src.applications.ui.page_objects.login_page import LoginPage


class GitHubUI:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.LoginPage = LoginPage(self)
        self.SingupPage = None

    def open(self):
        self.driver.get(CONFIG.get("BASE_URL_UI"))
        return self

    def check_repo_exists(repo_name):
        return True

    def quit(self):
        self.driver.quit()
