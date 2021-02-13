from userbot.google_imgs import googleimagesdownload
import os
import shutil
from re import findall
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern=r"img(?: |$)(\d*)? ?(.*)"))
async def img_sampler(event):
    if event.fwd_from:
        return
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_or_reply(
            event, "Reply to a message or pass a query to search!"
        )
    Lucifer = await edit_or_reply(event, "`Processing...`")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
    else:
        lim = int(5)
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await Lucifer.edit(f"Error: \n`{e}`")
    lst = paths[0][query]
    await event.client.send_file(event.chat_id, lst, reply_to=reply_message)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await Lucifer.delete()


CMD_HELP.update(
    {
        "images": "**Plugin :**`images`\
    \n\n**  •  Syntax :** `.img <limit> <Name>` or `.img <limit> (replied message)`\
    \n**  •  Function : **do google image search and sends 5 images. default if you havent mentioned limit"
    }
)
