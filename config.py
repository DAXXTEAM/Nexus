import os
from os import getenv


API_ID = int(getenv("API_ID", "24509589"))
API_HASH = getenv("API_HASH", "717cf21d94c4934bcbe1eaa1ad86ae75")
BOT_USERNAME = getenv("BOT_USERNAME", "Anzoobot")
BOT_TOKEN = getenv("BOT_TOKEN", "6576720076:AAFQiAq4XfW_t9hpfQRa8yYQNuRh2f1eGAs")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "")
