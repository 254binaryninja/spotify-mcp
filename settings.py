from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

## Load environment variables from .env file
load_dotenv()

## Create Settings class for accessing environment variables
class Settings(BaseSettings):
    #Application settings
    APP_NAME: str =  "spotify-mcp-server"

    #SPOTIFY credentials
    SPOTIFY_CLIENT_ID: str = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET: str = os.getenv("SPOTIFY_CLIENT_SECRET")

class Config:
    case_sensitive = True
    env_file = ".env"


settings = Settings()
