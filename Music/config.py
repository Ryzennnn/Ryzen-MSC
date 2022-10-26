##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv('SESSION_NAME')
API_ID = int(getenv('API_ID'))
API_HASH = getenv('API_HASH')

# Bot
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv('BOT_TOKEN')

# Music Setting
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())

# Database Mono
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Sudo
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split()))
OWNER_ID = list(map(int, getenv('OWNER_ID').split()))

# Log Chat
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID"))

# Assistant
ASS_ID = int(getenv("ASS_ID"))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))

# Support Channel
CHANNEL = getenv("CHANNEL", "Ryzen_Music")
GROUP = getenv("GROUP", "Ryzen_Music")

# Update Stream
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
REPO_URL = getenv("REPO_URL", "https://github.com/Ryzenstd/Ryzen-Music")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1kyeXl2d0MxdzBycFVkRlVMMUZjQ1hNQXd1TTFvNjIwVEZEbA==").decode(
        "utf-8"
    ),
)

# Heroku
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Broadcast
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
