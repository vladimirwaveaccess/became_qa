import os

from src.config.providers.config_from_env_provider import ConfigFromEnvProvider
from src.config.providers.config_from_json_provider import ConfigFromSimpleJsonProvider


class Config:
    default_env = "dev"

    def __init__(self) -> None:
        self.conf_dict = {}

        env = os.environ.get('ENV')
        if env is None:
            env = Config.default_env

        json_path = f"src/config/env_configs/{env}.json"

        self.providers = [
            ConfigFromSimpleJsonProvider(json_path),
            ConfigFromEnvProvider(),
            ]

        self.register("BASE_URL_API")
        self.register("BASE_URL_UI")

    def register(self, name):
        """
        Register name of the key which is used
        in tests
        """

        # Order in self.provider makes difference
        for provider in self.providers:
            if provider.get(name) is not None:
                self.conf_dict[name] = provider.get(name)

        # raise error if no value is found across the providers
        if self.conf_dict.get(name) is None:
            raise Exception(f"{name} variable is not set in config")

        print(f"{name} variable is registered in config with value {self.conf_dict.get(name)}")

    def get(self, name):
        """
        Return existing value
        """
        if self.conf_dict.get(name) is None:
            raise Exception(f"{name} variable is not set in config")

        return self.conf_dict.get(name)


# python way singleton
config = Config()