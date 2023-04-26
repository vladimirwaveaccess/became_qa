from src.config.providers.config_from_env_provider import ConfigFromEnvProvider


def test_config_env_provider_negative():
    # classical approach
    conf = ConfigFromEnvProvider()
    val = conf.get("KJHKJFHSDKJFH")
    assert val is None


class test_config_env_provider_positive():
    # better approach
    def __init__(self) -> None:
        conf = ConfigFromEnvProvider()
        self.val = conf.get("PATH")

    def test_val(self):
        assert self.val == "/home/vladimirwaveaccess/.poetry/bin:/home/vladimirwaveaccess/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"

    def test_check(self):
        assert self.val.check()

    def test_transform(self):
        assert self.val.transform()
