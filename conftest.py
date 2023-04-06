import pytest

from src.applications.api.github_api_client import GitHubApiClient
from src.config.config import config


@pytest.fixture
def github_api_client():
    github_api_client = GitHubApiClient()
    github_api_client.login(config.get("USERNAME"), config.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout()
