from selenium import webdriver
from selenium.webdriver.common.by import By

from src.config.config import config


class GitHubUI:
    def __init__(self):
        self.driver = None

    def launch(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def go_to_login_page(self):
        self.driver.get(config.get("BASE_URL_UI"))

    def try_login_to_login_page(self):
        input_login = self.driver.find_element(By.ID, 'login_field')
        input_login.click()
        input_login.clear()
        input_login.send_keys('qwerty')

        input_password = self.driver.find_element(By.ID, 'password')
        input_password.click()
        input_password.clear()
        input_password.send_keys('qwerty')

        sign_in_button = self.driver.find_element(By.NAME, 'commit')
        sign_in_button.click()

        return self.driver.find_element(By.XPATH, "//div[contains(text(),'Incorrect username or password.')]").text

    def check_error_message(self):
        assert self.try_login_to_login_page() == 'Incorrect username or password.'
