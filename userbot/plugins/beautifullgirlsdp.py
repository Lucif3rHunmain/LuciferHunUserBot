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

  "sara-jean-underwood-desktop-wallpapers",
  
  "kate-upton-wallpaper-1920x1080",

  "emma-stone-hd-wallpaper",

  "celebrities-wallpaper",

  "scarlet-witch-hd-wallpaper",
  
  "jessica-simpson-wallpapers",

  "ellie-goulding-wallpaper-hd",

  "katy-perry-hd-wallpaper-1920x1080",

  "most-beautiful-women-hd-wallpaper",

  "beautiful-ladies-wallpapers",

  "wallpapers-of-women",

  "hd-wallpapers-1080p-girls",

  "selena-gomez-2018-wallpaper",

  "pretty-girls-wallpapers",

  "latina-wallpapers"
]

async def bgirlspp():

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

@borg.on(admin_cmd(pattern="girlsdp ?(.*)"))

async def main(event):

    await event.edit("**Starting Girls Profile Pic...\n\nDone !!! Check Your DP **")
    while True:

        await girlspp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(300)
        
CMD_HELP.update({"beautifullgirlsdp": ".girlsdp\nUse - Auto-changing dp of Beautiful Girls."})
