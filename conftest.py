import pytest

from src.providers.service.browsers.browsers_provider import BrowsersProvider
from src.applications.api.github_api_client import GitHubApiClient
from src.applications.ui.github_ui_app import GitHubUI
from src.config.config import CONFIG


@pytest.fixture
def github_api_client():
    github_api_client = GitHubApiClient()
    github_api_client.login(CONFIG.get("USERNAME"), CONFIG.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout(CONFIG.get("USERNAME"))


@pytest.fixture
def github_ui_client():
    browser = CONFIG.get("BROWSER")
    driver = BrowsersProvider.get_driver(browser)

    ui_client = GitHubUI(driver)

    yield ui_client

    ui_client.quit()
