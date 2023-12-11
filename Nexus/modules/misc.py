from Nexus import Nexus
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *

@Nexus.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"ʏᴏᴜʀ ɪᴅ: {message.from_user.id}\n{reply.from_user.first_name}'s ɪᴅ: {reply.from_user.id}\nᴄʜᴀᴛ ɪᴅ: {message.chat.id}"
        )
    else:
        message.reply(
            f"ʏᴏᴜʀ ɪᴅ: {message.from_user.id}\nᴄʜᴀᴛ ɪᴅ: {message.chat.id}"
        )
