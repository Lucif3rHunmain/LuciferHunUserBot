
import asyncio
import os
import requests
import json
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, edit_delete, admin_cmd
from userbot.uniborgConfig import Config

VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)

@borg.on(admin_cmd(pattern="vtscan$", outgoing=True))
async def vtscan(event):
    if Config.VIRUSTOTAL_API_KEY is None:
        return await edit_delete(
            event, "Fill the Config VAR `VIRUSTOTAL_API_KEY` by getting the Api Key from https://virustotal.com/", 5
        )
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "`Reply to any media file !`", 5
        )
    catevent = await edit_or_reply(event, "`Downloading the file to check...`")
    media = await event.client.download_media(reply)
    catevent = await edit_or_reply(event, "`Scanning the file for any kind of virus or malware and abnormal behaviour. Please Wait...`")
    scanurl = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': VIRUSTOTAL_API_KEY}
    files = {'file': open(media, 'rb')}
    vresponse = requests.post(scanurl, files=files, params=params)
    os.remove(media)
    catevent = await edit_or_reply(event, vresponse.json())
    msg = vresponse.json()["vebrose_msg"]
    if msg.text.startswith("Scan rquest successfully queued"):
     catevent = await edit_or_reply(event, "File successfully uploaded for scanning. Wait for 1 mintues to get the scan results")
     await asyncio.sleep(10)
     catevent = await edit_or_reply(event, "File Scan Initialized")
     await asyncio.sleep(10)
     md5 = vresponse.json()["md5"]
     sha1 = vresponse.json()["sha1"]
     sha256 = vresponse.json()["sha256"]
     resource = vresponse.json()["resource"]
     reporturl = 'https://www.virustotal.com/vtapi/v2/file/report'
     params = {'apikey': Config.VIRUSTOTAL_API_KEY, 'resource': resource}
     response1 = requests.get(reporturl, params=params)
     catevent = await edit_or_reply(event, f,"File Hash \n Md5- {md5} \n Sha1- {sha1} \n Sha256- {sha256}")
     catevent = await edit_or_reply(event, response1.json())
    else:
     catevent = await edit_or_reply(event, vresponse.json())
CMD_HELP.update(
        {
        "VirusTotal": ".vtscan"
                      "\nUsage: Reply any media .vtscan command to any media file to scan it for malware or virus and any malicious behaviour. \n\n"
    }
)
