import asyncio
import os
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
    h = hashlib.sha1()
    with open(media , 'rb') as file:
       chunk = 0
    while chunk != b'':
         chunk = file.read(1024)
         h.update(chunk)
    return h.hexdigest()
    message = hash_file(media)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': Config.VIRUSTOTAL_API_KEY, 'resource': resource}
    response_2 = requests.get(url, params=params)
    response_code = response_2
    response_jso = json.load(response_2.text)
    verbose = response.jso['verbose_msg']
    if verbose == 'The requested resource is not among the finished, queued or pending scans':
      url = 'https://www.virustotal.com/vtapi/v2/file/scan'
      params = {'apikey': Config.VIRUSTOTAL_API_KEY} 
      files = {'file': (media, open(media, 'rb'))}
      response = requests.post(url, files=files, params=params)
      response_json = json.load(response.text)
      resource = response_json['resource']
      await asyncio.sleep(20)
      url = 'https://www.virustotal.com/vtapi/v2/file/report'
      params = {'apikey': Config.VIRUSTOTAL_API_KEY, 'resource': resource}
      response_2 = requests.get(url, params=params)
      response_jso = json.load(response_2.text)
      catevent = await edit_or_reply(event, response_jso)
  
CMD_HELP.update(
        {
        "VirusTotal": ".vtscan"
                      "\nUsage: Reply any media .vtscan command to any media file to scan it for malware or virus and any malicious behaviour. \n\n"
    }
)
