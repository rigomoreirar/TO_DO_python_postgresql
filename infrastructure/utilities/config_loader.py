import os
from dotenv import load_dotenv
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, env_path: str = '.env'):
        load_dotenv(dotenv_path=env_path)

    def get(self, key: str, default: Any = None) -> Any:
        return os.getenv(key, default)

    def get_all(self) -> Dict[str, Any]:
        return {key: os.getenv(key) for key in os.environ.keys()}