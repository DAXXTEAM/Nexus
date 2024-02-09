import asyncio
import importlib
from pyrogram import idle
from Nexus import Nexus
from Nexus.modules import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def Nex_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Nexus.modules." + all_module)
    print("""𝐘𝐨𝐮𝐫 𝐛𝐨𝐭 𝐡𝐚𝐬 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐚𝐧𝐝 𝐢𝐬 𝐫𝐞𝐚𝐝𝐲 𝐭𝐨 𝐚𝐬𝐬𝐢𝐬𝐭""")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(Nex_boot())
