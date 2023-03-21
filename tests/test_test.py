from src.config.config import config


def test_http_request():
    print(config.get("BASE_URL_API"))


def test_ui_pom():
    print(config.get("BASE_URL_UI"))
