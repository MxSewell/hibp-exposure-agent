import os
from dotenv import load_dotenv

load_dotenv()


def get_required_env(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Missing required environment variable: {var_name}")
    return value


ANTHROPIC_API_KEY = get_required_env("ANTHROPIC_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "claude-haiku-4-5-20251001")