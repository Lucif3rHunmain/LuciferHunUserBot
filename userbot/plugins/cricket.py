"""
Created by @Lucif3rHun
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd, edit_or_reply
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern=r"cricket (.*)"))
async def _(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str == "":
     await event.edit("Please give a correct command. Type `.help cricket` to know more")
     await asyncio.sleep(5)
     await event.delete
    else:
     input_cmd = int(input_str.split(" ", 2)[0])
     if input_cmd == 'score' or input_Time == 'Score':
      if event.fwd_from:
        return
        chat = "@cricbuzz_bot"
        reply_to_id = event.message
       lucievent = await edit_or_reply(event, "Gathering info...")
        async with event.client.conversation(chat) as conv:
         try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message("/score")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
         except YouBlockedUserError:
            await megaevent.edit("Unblock @cricbuzz_bot & try again")
            return
         if respond.text.startswith("I can't find that"):
            await lucievent.edit("sorry I can't find it")
         else:
            await lucievent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
         await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )
     elif input_cmd == 'recent' or input_cmd == 'Recent':
      if event.fwd_from:
        return
        chat = "@cricbuzz_bot"
        reply_to_id = event.message
        lucievent = await edit_or_reply(event, "Gathering info...")
        async with event.client.conversation(chat) as conv:
         try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message("/recent")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
         except YouBlockedUserError:
            await lucievent.edit("Unblock @cricbuzz_bot & try again")
            return
         if respond.text.startswith("I can't find that"):
            await lucivent.edit("sorry i can't find it")
         else:
            await megaevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )

     elif input_cmd == 'upcoming' or input_cmd == 'Upcoming':
       if event.fwd_from:
        return
        chat = "@cricbuzz_bot"
        reply_to_id = event.message
        lucivent = await edit_or_reply(event, "Gathering info...")
        async with event.client.conversation(chat) as conv:
         try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message("/upcoming")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
         except YouBlockedUserError:
            await megaevent.edit("Unblock @cricbuzz_bot & try again")
            return
         if respond.text.startswith("I can't find that"):
            await lucievent.edit("sorry i can't find it")
         else:
            await lucievent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
         await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )
     else:
      if event.fwd_from:
        return
     details = event.pattern_match.group(1)
     chat = "@cricbuzz_bot"
     reply_to_id = event.message
     lucievent = await edit_or_reply(event, "Collecting information...")
     async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(f"{details}")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await lucievent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await lucievent.edit("sorry i can't find it")
        else:
            await lucievent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )

CMD_HELP.update(
    {
        "cricket": "**Plugin :** cricket\
      \n\n**  • Syntax : **.cricket <score> \
      \n**  • Function : **__To see score of ongoing matches.__\
      \n\n**  • Syntax : **.cric <recent>\
      \n**  • Function : **__Recent Match Result.__\
      \n\n**  • Syntax : **.cric <upcoming>\
      \n**  • Function : **__To get results of upcoming match.__\
      \n\n**  • Syntax : **.cric <cmd>\
      \n**  • Function : **__To get details.__\
      \n\n**  • Example :-** .cric /score...."
    }
)
