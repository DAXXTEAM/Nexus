import os
from os import getenv


API_ID = int(getenv("API_ID", "24509589"))
API_HASH = getenv("API_HASH", "717cf21d94c4934bcbe1eaa1ad86ae75")
BOT_USERNAME = getenv("BOT_USERNAME", "Anzoobot")
BOT_TOKEN = getenv("BOT_TOKEN", "6315773312:AAGIs5C06gl3dnGy3UwanJ_xvy6OsfnL0hk")
OWNER_ID = int(getenv("OWNER_ID", "6691393517"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQBiMZkAxAHZ71oKkYVRJjSxVY0METclPvH6vLe07jJIvw80LWbxUCRPKfoMOmogdl2k9h4ohM_iZ7J-DRB-E0xU8XU8X9W1PktE6vrjVMKg6Nuv2DaKzRtboNk2SUBpwEK7unWrFOKGqb_YJ63b8CrjEfGJMr4dR2JBIQ2qI6mBxzbiUbYo9slX0pcGXHL1CP841tY7tEfid19QZlp8sbI1f8vyDXbnDn5b310h3kl9xUdC6EVAv07sacHSLtqC0urAZKaDWjAHLMxOACi570X-TNmmJPTzgi3ZAJhZzHMHNr6hvmlJ05koD1pkqJS-lENir2ahPc8SX_1P6SOPI3UHaDu4QwAAAAFsBedvAA")
CHANNEL = getenv("CHANNEL", "https://t.me/ALLTYPECC")
SUPPORT = getenv("SUPPORT", "https://t.me/HEROKUFREECC")
OWNER_USERNAME = getenv("OWNER_USERNAME","iam_daxx")
