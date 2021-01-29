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
  "Predator-Wallpapers-Backgrounds",
  "Alien-vs-Predator-Wallpaper"
]

async def ppp():
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
    
@borg.on(admin_cmd(pattern="predatordp ?(.*)"))
async def main(event):
    await event.edit("**Starting predator Profile Pic.**") #Owner @NihiNivi
    await asyncio.sleep(4)
    await event.delete()
    while True:
        await ppp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(300)
CMD_HELP.update({"predatordp": ".predatordp\nUse - Auto-changing dp of Predators."})
