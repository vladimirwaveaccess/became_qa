from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from src.config.config import CONFIG


class FFBrowser:

    @staticmethod
    def get_driver():
        options = None

        if CONFIG.get("DEBUG_MODE") is False:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
