from pyrogram import filters, Client
from config import OWNER_ID
from Nexus import Nexus
import random
from Nexus.Helper import *
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)



# ------------------------------------------------------------------------------- #







@Chizuru.on_message(group=10)
async def chat_watcher_func(_, message):
    try:
        if message.from_user:
            us_in_db = await get_user(message.from_user.id)
            if not us_in_db:
                await add_user(message.from_user.id)

        chat_id = (message.chat.id if message.chat.id != message.from_user.id else None)

        if not chat_id:
            return

        in_db = await get_chat(chat_id)
        if not in_db:
            await add_chat(chat_id)
    except:
        pass
        


# --------------------------------------------------------------------------------- #


@Chizuru.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(cli: Client, message: Message):
    users = len(await get_users())
    chats = len(await get_chats())
    await message.reply_photo("https://graph.org/file/2eb489e499193ad8f0f24.jpg",
        caption=f"""**ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ** {(await cli.get_me()).mention} :

➻ ᴄʜᴀᴛs : {chats}
➻ ᴜsᴇʀs : {users}
"""
    )
    
# --------------------------------------------------------------------------------- #
