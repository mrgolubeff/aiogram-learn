from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretSrt


class Settings(BaseSettings):
    bot_token: SecretSrt

    model_config = SettingsConfigDict(env_file='bot.config', env_file_encoding='utf-8')


config = Settings()