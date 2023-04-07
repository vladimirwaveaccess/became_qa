from src.config.config import config


def test_http_request():
    print(f'BASE_URL_API = {config.get("BASE_URL_API")}')
    print(f'USERNAME = {config.get("USERNAME")}')
    print(f'PASSWORD = {config.get("PASSWORD")}')


def test_ui_pom():
    print(f'BASE_URL_UI = {config.get("BASE_URL_UI")}')
    print(f'USERNAME = {config.get("USERNAME")}')
    print(f'PASSWORD = {config.get("PASSWORD")}')

