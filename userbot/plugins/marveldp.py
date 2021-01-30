import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd
from userbot import CMD_HELP

import asyncio

from time import sleep

COLLECTION_STRING = [

  "avengers-logo-wallpaper",

  "avengers-hd-wallpapers-1080p",

  "avengers-iphone-wallpaper",

  "iron-man-wallpaper-1920x1080",

  "iron-man-wallpapers",

  "Marvel-Shield-iPhone-Wallpaper",

  "Shield-Logo-Wallpaper",

  "Marvel-Shield-Logo-Wallpaper",

  "Agents-of-Shield-Wallpaper",

  "Agents-of-Shield-iPhone-Wallpaper",

  "Agents-of-Shield-Wallpapers-HD"

  "Thor-Wallpaper-1920x1080",

  "Thor-Wallpapers",

  "Avengers-HD-Wallpapers-1080p",

  "Avengers-Wallpaper-for-Desktop",

   "Avengers-4K-Wallpaper",

  "Avengers-Age-of-Ultron-Wallpaper",

  "Avengers-Civil-War-Wallpaper",

  "Avengers-2-Wallpapers",

  "Avengers-Logo-Wallpaper",

  "Marvel-Avengers-Desktop-Wallpaper",

  "4K-Deadpool-Wallpaper",

  "3D-Deadpool-Logo-Wallpaper",

  "Deadpool-HD-Desktop-Wallpaper",

  "Cool-Deadpool-Wallpaper",

  "Thor-Wallpaper-HD"
  
]

async def marvelpp():

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

@borg.on(admin_cmd(pattern="marveldp ?(.*)"))

async def main(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str == "":
     input1_Delay = 300
    else:
     input_Delay = int(input_str.split(" ", 2)[0])
     input_Time = str(input_str.split(" ", 2)[1])
     if input_Time == 'd' or input_Time == 'D':
      input1_Delay=(input_Delay*24*60*60)
     elif input_Time == 'h' or input_Time == 'H':
      input1_Delay=(input_Delay*60*60)
     elif input_Time == 'm' or input_Time == 'M':
      input1_Delay=(input_Delay*60)
     elif input_Time == 's' or input_Time == 'S':
      input1_Delay=input_Delay
     else:
      input1_Delay = 300

    await event.edit("**Starting Marvel Profile Pics... **")
    while True:

        await marvelpp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")
        await event.edit("**Done !!! Check Your DP**")
        await asyncio.sleep(3)
        await event.delete()
        await asyncio.sleep(input1_Delay)
CMD_HELP.update(
  {
    "Marvel DP": "`.marveldp`"
    "\nUsage - Auto-changing dp of Marvel Every 5 Mins(Default). \n\n"
    "`.marveldp` <delay> <s or S for seconds, m or M for minute(s) Delay, h or H for hour(s) Delay and d or D for Day(s) Delay>"
    "\nUsage - Auto-changing dp of Marvel with custom Delay. \n\n"
  }
)
