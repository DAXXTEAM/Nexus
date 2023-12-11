from pyrogram import filters
from Nexus import Nexus
from config import BOT_USERNAME
from pyrogram.types import *



START_TEXT = """
ʜᴇʟʟᴏ {} 


"""


button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),    
        ],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_"),    
        ]
])

@Nexus.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo("https://telegra.ph/file/65eeaaa6d9542513824d0.jpg",
                            caption=START_TEXT.format(message.from_user.mention),reply_markup=button)

