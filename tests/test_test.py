from src.config.config import config


def test_http_request():
    config.get("BASE_URL_API")
    print(config.get("BASE_URL_API"))


def test_ui_pom():
    print(f'qqqqqqqqqqqqqqqqqqqqqqqqqq {config.get("BASE_URL_UI")}')

