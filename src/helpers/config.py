from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str
    app_version: str  
    api_key: str
    file_type: list[str]
    max_file_size: int
    class Config:
        env_file = ".env"
        

def settings_loader():
    return Settings()

