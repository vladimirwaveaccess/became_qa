from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from src.config.config import CONFIG


class ChromeBrowser:

    @staticmethod
    def get_driver():
        options = Options()
        options.page_load_strategy = 'normal'

        if CONFIG.get("DEBUG_MODE") is False:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
