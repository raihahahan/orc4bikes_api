import os
from dotenv import load_dotenv

load_dotenv()

def check_token(token: str) -> bool:
    return token == os.getenv("TELEGRAM_BOT_TOKEN")