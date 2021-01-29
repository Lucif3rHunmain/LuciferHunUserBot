import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from userbot import CMD_HELP

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRING = [

  "indian-actress-wallpapers",

  "latest-bollywood-actress-wallpapers-2018-hd",

  "bollywood-actress-wallpaper",

  "hd-wallpapers-of-bollywood-actress",

  "new-bollywood-actress-wallpaper-2018"

]

async def actresspp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="actressdp ?(.*)"))
async def main(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    input_Delay = int(input_str.split(" ", 2)[0])
    input_Time = str(input_str.split(" ", 2)[1])
    if input_Time == 'h' or input_Time == 'H':
     input1_Delay=(input_Delay*60*60)
    elif input_Time == 'm' or input_Time == 'M':
     input1_Delay=(input_Delay*60)
    else:
      input1_Delay = 300

    await event.edit("**Starting Actress Profile Pic...\n\nDone !!! Check Your DP **")
    while True:

        await actresspp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(input1_Delay)

CMD_HELP.update({"actressdp": ".actressdp\nUse - Auto-changing dp of Indian Actress."})
