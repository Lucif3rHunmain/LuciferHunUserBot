"""
Created by @Lucif3rHun
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd, edit_or_reply
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern=r"cricket score"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@cricbuzz_bot"
    reply_to_id = event.message
    megaevent = await edit_or_reply(event, "Gathering info...")
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
            await megaevent.edit("sorry i can't find it")
        else:
            await megaevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )
     
@borg.on(admin_cmd(pattern=r"cricket recent"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@cricbuzz_bot"
    reply_to_id = event.message
    megaevent = await edit_or_reply(event, "Gathering info...")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message("/recent")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await megaevent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await megaevent.edit("sorry i can't find it")
        else:
            await megaevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )
@borg.on(admin_cmd(pattern=r"cricket upcoming"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@cricbuzz_bot"
    reply_to_id = event.message
    megaevent = await edit_or_reply(event, "Gathering info...")
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
            await megaevent.edit("sorry i can't find it")
        else:
            await megaevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )

@borg.on(admin_cmd(pattern=r"cricket (.*)"))
async def _(event):
    if event.fwd_from:
        return
    details = event.pattern_match.group(1)
    chat = "@cricbuzz_bot"
    reply_to_id = event.message
    megaevent = await edit_or_reply(event, "Collecting information...")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(f"{details}")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await megaevent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await megaevent.edit("sorry i can't find it")
        else:
            await megaevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )

CMD_HELP.update(
    {
        "cricket": "**Plugin :** cricket\
      \n\n**  • Syntax : **.cricket score \
      \n**  • Function : **__To see score of ongoing matches.__\
      \n\n**  • Syntax : **.cricket recent\
      \n**  • Function : **__Recent Match Result.__\
      \n\n**  • Syntax : **.cricket upcoming\
      \n**  • Function : **__To get results of upcoming match.__\
      \n\n**  • Syntax : **.cricket <cmd>\
      \n**  • Function : **__To get details.__\
      \n\n**  • Example :-** .cric /score...."
    }
)
