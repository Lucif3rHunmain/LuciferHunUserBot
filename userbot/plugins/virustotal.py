import asyncio
import os
import requests
imoprt hashlib
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
    
 def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""
   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("C:\\Users\\Tilak\\Downloads\\HOuITQC+.html")
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'Config.VIRUSTOTAL_API_KEY'}
    files = {'file': open(media, 'rb')}
    response = requests.post(url, files=files, params=params)
    result = response.json()
    catevent = await edit_or_reply(event, result)

CMD_HELP.update(
        {
        "VirusTotal": ".vtscan"
                      "\nUsage: Reply any media .vtscan command to any media file to scan it for malware or virus and any malicious behaviour. \n\n"
    }
)
