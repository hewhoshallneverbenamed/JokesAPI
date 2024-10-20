from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
# database
    database_hostname: str
    database_name: str
    database_username: str
    database_password: str
# jwt
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()