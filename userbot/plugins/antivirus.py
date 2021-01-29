#Copyright by Lucif3rHun, leech with credits leechers
import datetime
import asyncio
from telethon.tl.custom import Button
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"vtscan"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    
    chat = "@VirusTotalAV_bot"
    sender = reply_message.sender
    
    await event.edit("```Checking the file```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1356559037))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @VirusTotalAV_bot and try again```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else:
             await asyncio.sleep(10)
             await event.delete()
             await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)

@borg.on(admin_cmd(pattern=r"dtscan"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    
    chat = "@VS_Robot"
    sender = reply_message.sender
    
    await event.edit("```Checking the file```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=299969270))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @VS_Robot and try again```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else:
             await event.delete()
             await asyncio.sleep(10)
             await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)
CMD_HELP.update(
    {
        "Antivirus Scan": ".vtscan"
        "\nUsage: Scans the file from 61+ Antivirus\n\n"
        ".dscan"
        "\nUsage: Detailed scan of the file from Antivirus\n\n"
    }
)
