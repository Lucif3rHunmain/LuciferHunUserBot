import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep
from userbot import CMD_HELP

COLLECTION_STRING = [
  "star-wars-wallpaper-1080p",
  "4k-sci-fi-wallpaper",
  "star-wars-iphone-6-wallpaper",
  "kylo-ren-wallpaper",
  "darth-vader-wallpaper"
]

async def gamepp():
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
@borg.on(admin_cmd(pattern="gamerpfp ?(.*)"))
async def main(event):
    await event.edit("**Starting Gamer Profile Pic.**")
    await asyncio.sleep(4)
    await event.delete()
    while True:
        await gamepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(300)

CMD_HELP.update({"gamersdp": "`.gamerphp`\nUse - Auto-changing dp of Gamers."})
