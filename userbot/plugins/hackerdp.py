import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep
from userbot import CMD_HELP

COLLECTION_STRINGZ = [
  "hacker-background"
]

async def hackpp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="hacker ?(.*)"))

async def main(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
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
    await event.edit("**Starting Hacker Profile Pic...\n\nDone !!! Check Your DP")
    while True:

        await hackpp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(input1_Delay)

CMD_HELP.update(
  {
    "gamersdp": "`.hackerdp`\n"
    "Usage - Auto-changing dp of Gamers Every 5 Mins(Default)."
    "`.hackerdp <delay> <s or S for seconds, m or M for minute(s) Delay, h or H for hour(s) Delay and d or D for Day(s) Delay>`\n"
    "Usage - Auto-changing dp of Gamers with custom Delay."
  }
)