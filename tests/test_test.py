from src.config.config import CONFIG


def test_http_request():
    print(f'BASE_URL_API = {CONFIG.get("BASE_URL_API")}')
    print(f'USERNAME = {CONFIG.get("USERNAME")}')
    print(f'PASSWORD = {CONFIG.get("PASSWORD")}')


def test_ui_pom():
    print(f'BASE_URL_UI = {CONFIG.get("BASE_URL_UI")}')
    print(f'USERNAME = {CONFIG.get("USERNAME")}')
    print(f'PASSWORD = {CONFIG.get("PASSWORD")}')

