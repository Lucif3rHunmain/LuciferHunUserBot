import requests , re , random 
from userbot import CMD_HELP
import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep


# Space lovers 
COLLECTION_STRINGS = [

  "1920x1080-space-wallpapers",

  "4k-space-wallpaper",

  "cool-space-wallpapers-hd",
]

async def spacepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGS) - 1)

    pack = COLLECTION_STRINGS[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"friday.jpg")

@borg.on(admin_cmd(pattern="spacedp ?(.*)"))

async def main(event):

    await event.edit("**Starting Space Profile Pic...\n\nDone !!! Check Your DP") #Owner MarioDevs
    while True:

        await spacepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(input1_Delay)

CMD_HELP.update(
  {
    "gamersdp": "`.spacedp`\n"
    "Usage - Auto-changing dp of Gamers Every 5 Mins(Default)."
    "`.spacedp <delay> <s or S for seconds, m or M for minute(s) Delay, h or H for hour(s) Delay and d or D for Day(s) Delay>`\n"
    "Usage - Auto-changing dp of Gamers with custom Delay."
  }
)
