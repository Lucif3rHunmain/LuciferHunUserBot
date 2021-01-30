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
"girls-and-muscle-cars-wallpaper", 
"emma-stone-hd-wallpaper", 
"emma-watson-hd-wallpapers-1080p", 
"sexy-desktop-wallpapers-and-backgrounds", 
"beautiful-women-faces-wallpaper", 
"country-girl-wallpapers", 
"sofia-vergara-wallpaper-hd", 
"dirt-bike-girls-wallpaper", 
"girls-and-trucks-wallpapers", 
"sara-jean-underwood-desktop-wallpapers", 
"motorcycle-girl-wallpaper", 
"girls-on-motorcycles-wallpapers", 
"kaley-cuoco-wallpaper-1920x1080", 
"pin-up-girls-hd-wallpaper", 
"gorgeous-redhead-wallpaper", 
"melania-trump-wallpaper", 
"women-wallpapers-for-desktop", 
"kate-winslet-wallpapers-titanic", 
"taylor-momsen-wallpaper-hd", 
"danica-patrick-go-daddy-wallpapers", 
"katrina-kaif-wallpapers-hd", 
"jesse-jane-wallpapers", 
"wwe-paige-wallpaper", 
"kate-upton-wallpaper-1920x1080", 
"cute-teen-girl-wallpapers", 
"teenage-girl-wallpaper", 
"ellie-goulding-wallpaper-hd", 
"sasha-gray-wallpaper", 
"jessica-simpson-wallpapers", 
"marilyn-monroe-wallpaper", 
"car-girl-wallpapers", 
"teen-girl-wallpaper-for-computer", 
"miley-cyrus-wallpaper-23", 
"pretty-faces-wallpapers", 
"michelle-rodriguez-wallpaper-hd", 
"megan-fox-supergirl-wallpaper", 
"girl-and-bike-wallpaper", 
"emma-stone-wallpaper-1920x1080", 
"melanie-martinez-cry-baby-wallpaper", 
"pretty-girls-wallpapers", 
"pakistani-girl-wallpaper", 
"jojo-wallpaper", 
"jessica-chobot-wallpaper", 
"girls-surfing-wallpaper", 
"beauty-salon-wallpaper", 
"redhead-wallpaper", 
"scarlet-witch-hd-wallpaper", 
"emily-ratajkowski-wallpaper", 
"emma-watson-hd-wallpaper-1920x1080", 
"beautiful-ladies-wallpapers", 
"vault-girl-fallout-wallpapers", 
"taeyeon-wallpaper-2018", 
"amy-lee-hd-wallpaper", 
"military-pin-up-wallpaper", 
"jessica-simpson-daisy-duke-wallpaper", 
"water-girl-wallpaper", 
"iphone-girl-wallpapers", 
"surfer-girl-wallpaper", 
"chopper-girls-motorcycle-wallpaper", 
"ford-mustang-wallpaper-with-girls"'
"scene-girl-wallpaper", 
"wwe-divas-hd-wallpaper", 
"felicia-day-wallpaper", 
"carmen-electra-wallpaper-hd", 
"natalie-dormer-wallpaper", 
"punk-girl-wallpaper", 
"celebrities-wallpaper", 
"jennifer-lawrence-wallpaper-hd", 
"milla-jovovich-wallpaper", 
"pretty-girls-wallpaper", 
"katy-perry-hd-wallpaper-1920x1080", 
"wallpapers-of-women", 
"girls-wallpaper-desktop-background", 
"selena-gomez-2018-wallpaper", 
"latina-wallpapers", 
"kristin-kreuk-wallpaper-hd", 
"girls-with-guns-wallpaper", 
"country-girls-and-trucks-wallpaper", 
"tattoo-girl-wallpaper-hd", 
"maria-brink-hd-wallpaper", 
"wallpapers-and-screensavers-girls", 
"girl-skateboard-wallpaper", 
"cute-baby-girl-pictures-wallpapers", 
"gamer-girl-wallpaper", 
"most-beautiful-women-hd-wallpaper", 
"jordan-carver-wallpapers"
]


async def girlspp():

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

    await event.edit("**Starting Beautiful Girls Profile Pics... **")
    while True:

        await actresspp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")
        await event.edit("**Done !!! Check Your DP**")
        await asyncio.sleep(3)
        await event.delete()
        await asyncio.sleep(input1_Delay)
        
CMD_HELP.update(
  {
    "Beutiful Girls DP": "`.girlsdp`"
    "\nUsage - Auto-changing dp of Beutiful Girls Every 5 Mins(Default). \n\n"
    "`.girlsdp` <delay> <s or S for seconds, m or M for minute(s) Delay, h or H for hour(s) Delay and d or D for Day(s) Delay>"
    "\nUsage - Auto-changing dp of Beautiful Girls with custom Delay. \n\n"
  }
)
