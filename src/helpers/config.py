from pydantic_settings import BaseSettings, SettingsConfigDict

class settings(BaseSettings):
    """Settings class to load environment variables from .env file and provide configuration settings for the application."""
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    MONGODB_URL: str
    MONGODB_DATABASE: str

    # Define your configuration settings here
    # For example:
    class Config:
         env_file = ".env"

def get_settings():
    """Function to get the settings instance."""
    return settings()