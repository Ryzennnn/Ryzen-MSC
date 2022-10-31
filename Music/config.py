##Config

import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
get_queue = {}

# Client
SESSION_NAME = getenv('SESSION_NAME', 'BQApymvEihSArb-elRYwkLACQ5VV7p7YtxiNnX_JGtGK3Gd-dgBDvhpx1pUQJjWAvR2SuNXeGMLBxV5NbZKmRJJud9IVhWFNu_zOjWByKDqHE4A2k9yqL7Kcz6GrWBYT7HNxtqQ651wjOaCB3YmgCMQBkODVhA9mCHCVo8M8_p-YOB15bXUNe98eOK33gwXXaE3_HIGtx9EY9M5C6Oiq4OycEcsVm3L_kVVU_n9RkkPoEfz_dXxjSPXfMZ1RISRrTBjGRO6qZUzLAOQb7zPdcWkGUEE4eVwkrK8POLzdHVXGD1d59s937K9n1RlBFSflyxRIIscg0x02jP977NFEbHAheb4-yAA')
API_ID = int(getenv('API_ID', '23184709'))
API_HASH = getenv('API_HASH', 'f99dd916ef41cf47ee094f771855468d')

# Bot
BOT_USERNAME = getenv("BOT_USERNAME", "ryzenmusicbot")
BOT_TOKEN = getenv('BOT_TOKEN', '5561364640:AAGkgktSUqzaQ_Fubfv6Xp0nzIoESQdiLBA')

# Music Setting
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '5600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())

# Database Mongo
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://anest:anest@cluster0.osfukxh.mongodb.net/?retryWrites=true&w=majority")

# Sudo
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1209395963').split()))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1534983792').split()))

# Log Chat
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001678126928"))
LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID", "-1001844138965"))

# Assistant
ASS_ID = int(getenv("ASS_ID", "2042511048"))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))

# Support Channel
CHANNEL = getenv("CHANNEL", "Zarchxyz")
GROUP = getenv("GROUP", "Exclusivedating")

# Update Stream
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
REPO_URL = getenv("REPO_URL", "https://github.com/muhammadrizky16/KyyMusic")
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
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "True"))

OWNER_ID.append("1209395963")
OWNER_ID.append("1534983792")
