import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8179819065:AAGk6xDOJ6Fozh7P7-lIUgUqnijBw-mb8pU")  # Ensure correct key name
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN is missing from environment variables.")
        
    API_ID = int(os.environ.get("API_ID", "29538829"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "0098baaaa11b512a0a8b8eaf33a4d91a")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "1118716436").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "Alex")  # Making CREDIT an environment variable for flexibility
