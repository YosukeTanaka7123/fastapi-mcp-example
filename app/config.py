from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    version: str = "0.0.0"
    line_access_token: str = "YOUR_ACCESS_TOKEN"
    open_weather_api_key: str = "YOUR_OPEN_WEATHER_API_KEY"

    model_config = SettingsConfigDict(env_file=".env")
