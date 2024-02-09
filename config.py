import os
from os import getenv

API_ID = int(getenv("API_ID", None))

API_HASH = getenv("API_HASH", None)

BOT_USERNAME = getenv("BOT_USERNAME", None)

BOT_TOKEN = getenv("BOT_TOKEN", None)

OWNER_ID = int(getenv("OWNER_ID", None))

SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split())) if getenv("SUDO_USERS", None) else []

MONGO_URL = getenv("MONGO_URL", None)

SESSION_STRING = getenv("SESSION_STRING", None)

CHANNEL = getenv("CHANNEL", None)

SUPPORT = getenv("SUPPORT", None)

OWNER_USERNAME = getenv("OWNER_USERNAME", None)

PING_PIC = ["https://telegra.ph/file/7c25ef427c9f3cded5577.jpg","https://telegra.ph/file/625d235cc0a22fb8525b5.jpg","https://telegra.ph/file/1c62254d59baf7f968ba7.jpg","https://telegra.ph/file/7a0553bd4664486ab3008.jpg","https://telegra.ph/file/7b4dfa606e6f23961d30e.jpg", "https://telegra.ph/file/2773dec98d87b8562618c.jpg", "https://telegra.ph/file/80353d02e0368b71d2666.jpg","https://telegra.ph/file/6e5331dc4bef87464ea1c.jpg","https://telegra.ph/file/199a2e44cb8e77bb21b34.jpg","https://telegra.ph/file/8371bcd8952d089f9ec05.jpg","https://telegra.ph/file/f970e559dd1bb96fced1a.jpg","https://telegra.ph/file/59a305f8ce0c4e85949cc.jpg"]