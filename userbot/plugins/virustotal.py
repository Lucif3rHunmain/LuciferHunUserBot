
import asyncio
import os
import requests
import jsons
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, edit_delete, admin_cmd
from userbot.uniborgConfig import Config

VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
@borg.on(admin_cmd(pattern="vtscan$", outgoing=True))
async def detect(event):
    if Config.DEEP_AI is None:
        return await edit_delete(
            event, "Add VAR `` and get API get from http://www.virustotal.com", 5
        )
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "`Reply to a media file!`", 5
        )
    catevent = await edit_or_reply("`Downloading the file to check...`")
    media = await event.client.download_media(reply)
    catevent = await edit_or_reply("`Scanning the file for any kind of virus or malware and abnormal behaviour`")
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': VIRUSTOTAL_API_KEY}
    files = {'file': open(media, 'rb')}
    response = requests.post(url, files=files, params=params)
    vresponse = json.loads(response)
    vebrose_msg = vresponse["vebrose_msg"]
    if vebrose_msg.text.startswith("Scan rquest successfully queued,come back later for the report")
    catevent = await edit
    print(response.json())
    catevent = await edit_or_reply(event,f"{response.json()}")
    os.remove(media)
CMD_HELP.update(
        {
        "VirusTotal": ".vtscan"
                      "\nUsage: Reply any media .vtscan command to any media file to scan it for malware or virus and any malicious behaviour. \n\n"
    }
)
