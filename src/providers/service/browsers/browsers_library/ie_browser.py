from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from src.config.config import CONFIG


class IEBrowser:

    @staticmethod
    def get_driver():
        options = Options()
        options.page_load_strategy = 'normal'

        if CONFIG.get("DEBUG_MODE") is False:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        return webdriver.Edge(
            service=Service(verbose=True),
            options=options
        )
