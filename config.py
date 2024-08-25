from os import getenv

API_ID = int(getenv("API_ID", "21415583"))
API_HASH = getenv("API_HASH", "537124a5f4131e215aa2aefafae96db4")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7379512533").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/ef7782ca71ddef38077ce.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/Mrdadgoku/New-Userbot")
BRANCH = getenv("BRANCH", "main")
