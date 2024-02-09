from pyrogram import Client, filters
from Nexus import Nexus
import time
import random
from config import BOT_USERNAME, CHANNEL, SUPPORT, OWNER_USERNAME, OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message

# ------------------------------------------------------------------------------- #

NEX_PIC = [
    "https://telegra.ph/file/7c25ef427c9f3cded5577.jpg",
    "https://telegra.ph/file/625d235cc0a22fb8525b5.jpg",
    "https://telegra.ph/file/1c62254d59baf7f968ba7.jpg",
    "https://telegra.ph/file/7a0553bd4664486ab3008.jpg",
    "https://telegra.ph/file/7b4dfa606e6f23961d30e.jpg",
    "https://telegra.ph/file/2773dec98d87b8562618c.jpg",
    "https://telegra.ph/file/80353d02e0368b71d2666.jpg",
    "https://telegra.ph/file/6e5331dc4bef87464ea1c.jpg",
    "https://telegra.ph/file/199a2e44cb8e77bb21b34.jpg",
    "https://telegra.ph/file/8371bcd8952d089f9ec05.jpg",
    "https://telegra.ph/file/f970e559dd1bb96fced1a.jpg",
    "https://telegra.ph/file/59a305f8ce0c4e85949cc.jpg"
]
# ------------------------------------------------------------------------------- #


HELP_TEXT = """
ʜᴇʟʟᴏ {} 
\n⋆─────────────────────⋆
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ  ᴄᴏᴍᴍᴀɴᴅs:
⦿ /play ➠ ᴘʟᴀʏs ᴀ sᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.
⦿ /vplay  ➠ ᴘʟᴀʏs ᴀ sᴏɴɢ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ.
⦿ /porn  ➠sᴏᴏɴ.
⦿ /stop ➠ sᴛᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴏɴɢ.
⦿ /end ➠ ᴇɴᴅs ᴛʜᴇ ᴍᴜsɪᴄ ᴘʟᴀʏʙᴀᴄᴋ.
⦿ /skip ➠ sᴋɪᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴏɴɢ.
⦿ /volume ➠ ᴀᴅᴊᴜsᴛs ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ʟᴇᴠᴇʟ.
⦿ /song ➠ ᴅᴏᴡɴʟᴏᴀᴅ ғᴏʀ ᴀ sᴏɴɢ.
⦿ /video ➠ ᴅᴏᴡɴʟᴏᴀᴅ ғᴏʀ ᴀ ᴠɪᴅᴇᴏ.
⦿ /id ➠ ᴅɪsᴘʟᴀʏs ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ ᴏʀ ɢʀᴏᴜᴘ ɪᴅ.
"""
# ------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------- #

@Nexus.on_message(filters.command("help"))
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(NEX_PIC),
        caption=HELP_TEXT.format(message.from_user.mention, message.from_user.id)
    )
# ------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------
