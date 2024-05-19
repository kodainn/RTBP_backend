import os
from dotenv import load_dotenv

load_dotenv()

def get_env_value(key: str) -> str:
    return str(os.getenv(key))