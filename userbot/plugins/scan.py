import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
from userbot import bot, CMD_HELP

@borg.on(admin_cmd(pattern="scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to any user message.")
       return
    reply_message = await event.get_reply_message() 
    chat = "@tgscanrobot"
    sender = reply_message.sender.id
    if reply_message.sender.bot:
       await event.edit("Reply to actual users message.")
       return
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              #await conv.send_message("/search_id {}".format(sender))
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=1557162396))
              await conv.send_message('{}'.format(sender))
              response1 = await response1
          except YouBlockedUserError:
              await event.reply("Please unblock bot ")
              return
          if response1.text.startswith("No records found"):
             await event.edit("User never changed his Username...")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response1.message)

CMD_HELP.update(
    {
        "ScanGroup": "__**PLUGIN NAME :** ScanGroup__\
    \n\nðŸ“Œ** CMD â˜…** `.scan`\
    \n**USAGE   â˜…  **Retrieves the Number and Names of the Groups the User Joined"
    }
)
