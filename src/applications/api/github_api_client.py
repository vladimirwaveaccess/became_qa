import requests

from src.config.config import config
from src.data.local_links import URL_SEARCH_REPO


class GitHubApiClient:

    def __init__(self) -> None:
        self.token = None

    def search_repo(self, repo_name):
        """Request method for search"""
        body = requests.get(
            url=self._form_url(URL_SEARCH_REPO),
            params={'q': repo_name},
            timeout=3000
        )
        return body.json()

    def search_repo_without_param(self):
        """Request method for search without param"""
        body = requests.get(
            url=self._form_url(URL_SEARCH_REPO),
            timeout=3000
        )
        return body.json()

    def login(self, username, password):
        print(f"Do login with {username}:{password}")
        self.token = "test_token"

    def logout(self, username):
        print(f"Do logout for {username}")

    def _form_url(self, url):
        return config.get("BASE_URL_API") + url
