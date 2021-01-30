
import asyncio
import os
import requests
import json
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, edit_delete, admin_cmd
from userbot.uniborgConfig import Config

VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)

@borg.on(admin_cmd(pattern="vtscan$", outgoing=True))
async def detect(event):
    if Config.VIRUSTOTAL_API_KEY is None:
        return await edit_delete(
            event, "Add VAR `VIRUSTOTAL_API_KEY` and get API get from http://www.virustotal.com", 5
        )
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit(
            "`Reply to a media file!`", 5
        )
    await event.edit("`Downloading the file to check...`")
    media = await event.client.download_media(reply)
    await event.edit("`Scanning the file for any kind of virus or malware and abnormal behaviour`")
    scanurl = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': VIRUSTOTAL_API_KEY}
    files = {'file': open(media, 'rb')}
    vresponse = requests.post(scanurl, files=files, params=params)
    jresponse = json.loads(vresponse)
    vebrose_msg = jresponse["vebrose_msg"]
    vebrose_msg.text.startswith("Scan rquest successfully queued,come back later for the report")
    await event.edit("File successfully uploaded for scanning. Wait for 1 mintues to get the scan results")
    await event.edit("File Scan Initialized")
    await asyncio.sleep(10)
    md5 = jresponse["md5"]
    sha1 = jresponse["sha1"]
    sha256 = jresponse["sha256"]
    resource = jresponse["resource"]
    reporturl = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': Config.VIRUSTOTAL_API_KEY, 'resource': resource}
    response1 = requests.get(reporturl, params=params)
    await event.edit(f,"File Hash \n Md5- {md5} \n Sha1- {sha1} \n Sha256- {sha256}")
    await event.edit(response1.json())
    os.remove(media)
CMD_HELP.update(
        {
        "VirusTotal": ".vtscan"
                      "\nUsage: Reply any media .vtscan command to any media file to scan it for malware or virus and any malicious behaviour. \n\n"
    }
)
