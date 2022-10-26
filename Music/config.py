##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv('BQBs9IKUI_BjKSXH1IBYUzlPEzzkkvCBctzq-DxssRpI6W3c6GyhcpWySgVRH6qetCrLB1hO8TO6gqxUB4tcxA0QiTM5X3dnCFtgIIoPIF_VqcZm4IS1mQFmj4a7TYuyGcc0lJdjknm65azxF7zzBjiwYhkrbKeB0KWfzXV-GcNeNA7BwT2v-nDZLDAPFxP7B8bIhTTnMHKFExrBs7yVxkPi6sfqRk33sch71uRhHBnKMKsomvlH8gR1kVwxbpVITNtVES_6G8nQBovin8wqkgB0H5GuODG7aZJTBxsj0-x8kW39TdSTAvvMeLeaaib2sTS7G8LD2THRbbMa1ZVtwPgPeb4-yAA')
API_ID = int(getenv('23184709'))
API_HASH = getenv('f99dd916ef41cf47ee094f771855468d')

# Bot
BOT_USERNAME = getenv("ryznmusicbot")
BOT_TOKEN = getenv('5524682825:AAF-R88Hx_AfetXZMg1_ykuz0Ti_psBOO6k')

# Music Setting
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())

# Database Mono
MONGO_DB_URI = getenv("mongodb+srv://zennmusic:zennmusic@cluster0.jimla2w.mongodb.net/?retryWrites=true&w=majority")

# Sudo
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split()))
OWNER_ID = list(map(int, getenv('OWNER_ID').split()))

# Log Chat
LOG_GROUP_ID = int(getenv("-1001889413117"))
LOG_CHANNEL_ID = int(getenv("-1001858010993"))

# Assistant
ASS_ID = int(getenv("2042511048"))
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

SUDO_USERS.append("2042511048")
OWNER_ID.append("1534983792")
