#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27680154"))
API_HASH = environ.get("API_HASH", "a315daaf1bea7f1eaf4001fc6d951b17")
BOT_TOKEN = environ.get("BOT_TOKEN", "8152730088:AAF5AmzheYS9c_1T3YYHxNW3fMQaE3zyunE")
OWNER = int(environ.get("OWNER", "5425691569"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5425691569').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
