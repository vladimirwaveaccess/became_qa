import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseAPP:

    def __init__(self, driver) -> None:
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def click(self, locator):
        el = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        el.click()

        return True

    def type_text(self, locator, text):
        el = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

        return True

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).text

    def wait_loaded(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
