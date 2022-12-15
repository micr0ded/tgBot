from pydantic import BaseSettings, Field

class Auth_data(BaseSettings):
    API_ID: str
    API_HASH: str
    PHONE_NUMBER: str

    class Config:
        env_file = ".env"

auth_data = Auth_data()