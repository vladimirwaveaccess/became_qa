from src.config.config import config


def test_search_repo():
    assert 1 == 1


def test_config():
    print(config.get("BASE_URL"))
