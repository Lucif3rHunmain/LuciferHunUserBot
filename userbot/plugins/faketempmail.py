import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot import bot, CMD_HELP

@borg.on(admin_cmd("ftmail ?(.*)"))
async def _(event):

    chat = "@fakemailbot"
    await event.edit("```Getting you a fakemail My Master```")
    async with borg.conversation(chat) as conv:
          try:
              await conv.send_message('/generate')
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=177914997))
              response = await response
              a = response.replace('Your new fake mail id is ' , '')
              b = a.replace(' send /id to see the full list.' , '')
          except YouBlockedUserError: 
              await event.reply("```Please unblock @fakemailbot and try again```")
              return
          if response.text.startswith("send"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          elif response.text.startswith("An error occured"):
             await conv.send_message('/generate')
             response = conv.wait_event(events.NewMessage(incoming=True,from_users=177914997))
             response = await response
             a = response.replace('Your new fake mail id is ' , '')
             b = a.replace(' send /id to see the full list.' , '')
             await event.edit(f"Your new fake mail id is '{b}'.")
          else:
             await event.edit(f"Your new fake mail id is '{b}'.")

@borg.on(admin_cmd("ftmaills ?(.*)"))
async def _(event):

    chat = "@fakemailbot"
    await event.edit("```Getting you a fakemail My Master```")
    async with borg.conversation(chat) as conv:
          try:
              await conv.send_message('/id')
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=177914997))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @fakemailbot and try again```")
              return
          if response.text.startswith("send"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          elif response.text.startswith("An error occured"):
             await conv.send_message('/id')
             response = conv.wait_event(events.NewMessage(incoming=True,from_users=177914997))
             response = await response
             await event.edit(f"{response.message.message}")
          else: 
             await event.edit(f"{response.message.message}")

CMD_HELP.update(
    {
        "Fakemail": "__**PLUGIN NAME :** Tempmail__\
    \n\n📌** CMD ★** `.ftmail`\
    \n**USAGE   ★  **Get yourself a Tempmail without going to web\
    \n\n📌** CMD ★** `.ftmaills`\
    \n**USAGE   ★  **Gets you the list of fake temp mails you generated."

}
)
