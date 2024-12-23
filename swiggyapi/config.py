from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    dev_db_url:str 
    class Config:
        env_file = ".env"

settings = Settings()

