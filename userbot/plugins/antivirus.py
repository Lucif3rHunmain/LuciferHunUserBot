#Copyright by Lucif3rHun, leech with credits leechers
import datetime
import asyncio
from telethon.tl.custom import Button
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd

@borg.on(admin_cmd("scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to a media message```")
       return

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
          	if response.text.startswith("Select"):
          		await event.edit("`Please go to` @VirusTotalAV_bot `and select your language.`") 
          else:
          	await event.edit(f"Antivirus scan was completed.\n  Results  \n {response.message.message}")


@borg.on(admin_cmd("scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to a media message```")
       return
    
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
          	if response.text.startswith("Select"):
          		await event.edit("`Please go to` @VS_Robot `and select your language.`") 
          else:
          	await event.edit(f"Antivirus scan was completed.\n  Results  \n {response.message.message}")
CMD_HELP.update(
    {
        "Antivirus Scan": ".vtscan"
        "\nUsage: Scans the file from 61+ Antivirus\n\n"
        ".dscan"
        "\nUsage: Detailed scan of the file from Antivirus\n\n"
    }
)
