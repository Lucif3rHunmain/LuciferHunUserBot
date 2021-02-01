import asyncio
import os
import re
import requests
import hashlib
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
    catevent = await edit_or_reply(event, "`Uploading the file to virustotal.com for scanning it`")
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': Config.VIRUSTOTAL_API_KEY} 
    files = {'file': open(media, 'rb')}
    response = requests.post(url, files=files, params=params)
    response_json = json.loads(response.text)
    catevent = await edit_or_reply(event, "`Uploaded the file to virustotal.com and inistialized the scanning`")
    await event.edit(f"{response_json}")
    await asyncio.sleep(5)
    resource = response_json['resource']
    catevent = await edit_or_reply(event, "`Waiting for the scan to complete. Hang on a while!!`")
    await asyncio.sleep(60)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': Config.VIRUSTOTAL_API_KEY, 'resource': resource}
    response_2 = requests.get(url, params=params)
    await event.edit("`Getting Results`")
    await event.edit("`Got the Results, wait sending the results`") 
    await asyncio.sleep(5)
    a = response.text
    b = a.replace('}, "', '\n')
    c = b.replace('{"scans": {"', '')
    d = c.replace(' {"detected": ', '')
    e = re.sub('"version": ".*", ', '', d)
    f = re.sub('"result": .*,', '', e)
    g = re.sub(',  "update": ".*', '', f)
    h = re.sub('scan_id": .*, "', '', g)
    i = re.sub('md5": ".*"}', '', h)
    j = i.replace('":', ":")
    await event.edit(f"{j}")
  
CMD_HELP.update(
        {
        "VirusTotal": ".vtscan"
                      "\nUsage: Reply any media .vtscan command to any media file to scan it for malware or virus and any malicious behaviour. \n\n"
    }
)
