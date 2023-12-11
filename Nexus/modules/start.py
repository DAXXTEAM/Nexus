from pyrogram import filters
from Nexus import Nexus
import time
import random
from config import BOT_USERNAME, CHANNEL, SUPPORT, OWNER_USERNAME
from pyrogram.types import *


NEXUS_PIC = [
"https://telegra.ph/file/2e85d11aefdf6cd01301b.jpg",
"https://telegra.ph/file/0a08b180583f13952336a.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/bb0a28259990c6a978985.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/a0db46dfacd94e489117b.jpg",
"https://telegra.ph/file/cd77be2595cdc2fca60a3.jpg",
"https://telegra.ph/file/632724b3d30c691247c77.jpg",
"https://telegra.ph/file/a2d01afe4f2cb1d4b650c.jpg",
"https://telegra.ph/file/94dc035df11dfb159b999.jpg",
"https://telegra.ph/file/fed9a5b1cbaaefc3a818c.jpg",
"https://telegra.ph/file/66fd03632cbb38bdb4193.jpg"

]


START_TEXT = """
ʜᴇʟʟᴏ {} 
\n
Wᴇʟᴄᴏᴍᴇ \n
Iᴍᴍᴇʀsᴇ ʏᴏᴜʀsᴇʟғ ɪɴ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ\n
Dɪsᴄᴏᴠᴇʀ, ᴘʟᴀʏ, ᴀɴᴅ ᴇɴJᴏʏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴛᴜɴᴇs ʀɪɢʜᴛ ʜᴇʀᴇ\n
Sɪᴍᴘʟʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ sᴏɴɢ ᴏʀ ᴀʀᴛɪsᴛ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴇʟᴏᴅʏ ʙᴇɢɪɴ. \n
Usᴇ /Help ғᴏʀ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs. 🎶

"""


button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),    
        ],
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"{CHANNEL}"),
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"{SUPPORT}"),   
        ],
        [
                InlineKeyboardButton("ᴅᴇᴠ", url=f"t.me/{OWNER_USERNAME}"),
        ],
        [
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", callback_data="help_"),    
        ]
        
])

@Nexus.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(
          random.choice(NEXUS_PIC),
                            caption=START_TEXT.format(message.from_user.mention),reply_markup=button)



  
