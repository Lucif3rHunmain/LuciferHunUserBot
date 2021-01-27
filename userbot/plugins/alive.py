# Thanks to Sipak bro and Aryan
# Made by @hellboi_atul.
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"

# Thanks to Sipak bro and Aryan.. 
# Made by @hellboi_atul and Edited by Lucif3rHun
# Kang with credits else gay...
# alive.py for Lucif3rHun's Personal UserBot
global Lucif3r
Lucif3r = borg.uid
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/771b6db93ddc361f75a6e.jpg"
""" =======================CONSTANTS====================== """
@borg.on(admin_cmd(pattern="alive"))
async def alive(yes):
    await yes.get_chat()
    global Lucif3r
    Lucif3r = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** ʟᴜᴄɪғ𝟹ʀʜᴜɴ's ᴜsᴇʀʙᴏᴛ 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
    pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ About My System ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ʟᴜᴄɪғ𝟹ʀʜᴜɴ](https://github.com/Lucif3rHunmain)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [𝙳𝙰𝚁𝙺-𝙲𝙾𝙱𝚁𝙰](https://github.com/DARK-COBRA/DARKCOBRA)\n"
    pm_caption += "➾ **ᴇᴅɪᴛᴇᴅ ʙʏ** ☞ [ʟᴜᴄɪғ𝟹ʀʜᴜɴ](@Lucif3rHun)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={Lucif3r})\n"
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)
    await asyncio.sleep(10)
    await on.delete()
