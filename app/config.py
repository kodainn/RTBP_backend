from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

def get_env_value(key: str) -> Optional[str]:
    return os.getenv(key)