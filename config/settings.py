
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

settings = Settings()
