import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime
from userbot import CMD_HELP

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRING = [

  "angel-with-a-shotgun-wallpaper",
  "rwby-blake-wallpaper",
  "animated-angel-wallpaper",
  "anime-boy-wallpaper-hd",
  "tokyo-ghoul-wallpaper-hd",
  "pokemon-wallpaper-pikachu",
  "sasuke-wallpaper-hd",
  "anime-cat-girl-wallpaper",
  "anime-neko-wallpapers",
  "pokemon-serena-wallpaper",
  "black-bullet-wallpaper-hd",
  "anime-girls-wallpapers",
  "cute-anime-wallpapers-hd",
  "anime-christmas-wallpaper-hd",
  "anime-samurai-girl-wallpaper",
  "4k-anime-wallpapers",
  "2560-x-1440-wallpaper-anime",
  "cute-anime-wallpaper-1920x1080",
  "kakashi-hatake-wallpaper-hd",
  "dbz-broly-wallpaper",
  "anime-hatsune-miku-wallpaper",
  "attack-on-titan-chibi-wallpaper",
  "naruto-vs-sasuke-hd-wallpaper",
  "super-saiyan-god-goku-wallpaper",
  "1440p-anime-wallpaper",
  "tokyo-ghoul-kaneki-ken-wallpaper",
  "sasuke-uchiha-hd-wallpaper",
  "sharingan-wallpaper-hd-1920x1080",
  "2560-x-1080-anime-wallpaper",
  "anime-warrior-wallpaper",
  "anime-wallpaper-hd-1920x1080",
  "2560-x-1440-wallpaper-anime",
  "female-anime-samurai-wallpaper",
  "kiznaiver-wallpaper",
  "anime-wallpaper-1080x1920",
  "4k-anime-wallpapers",
  "shisui-uchiha-wallpapers",
  "anime-desktop-wallpaper",
  "dragon-ball-gt-wallpaper-hd",
  "anime-gamer-girl-wallpaper",
  "eren-and-levi-wallpaper",
  "aizen-wallpaper-hd",
  "frieza-wallpaper",
  "levi-attack-on-titan-wallpaper",
  "anime-valentines-day-wallpaper",
  "sailor-moon-wallpaper-1920x1080",
  "anime-assassin-wallpaper",
  "anime-yuri-wallpaper",
  "anime-samurai-girl-wallpaper",
  "japanese-anime-wallpapers-manga",
  "sasuke-and-itachi-wallpaper-hd",
  "samurai-champloo-wallpapers",
  "anime-wallpaper-1920x1080",
  "sword-art-online-2-wallpaper",
  "anime-music-wallpaper",
  "kuroko-basketball-wallpaper",
  "boruto-wallpaper-hd",
  "sao-wallpapers",
  "arpeggio-of-blue-steel-wallpaper",
  "red-and-black-anime-wallpaper",
  "naruto-nine-tails-wallpaper",
  "4k-anime-wallpaper",
  "inuyasha-wallpaper-hd",
  "super-saiyan-2-gohan-wallpaper",
  "kaneki-tokyo-ghoul-wallpaper",
  "yu-gi-oh-dark-magician-wallpaper",
  "jiraiya-wallpaper-hd",
  "high-quality-anime-wallpapers",
  "anime-vampire-girl-wallpaper",
  "sword-art-online-wallpaper-kirito",
  "anime-guy-wallpaper-hd",
  "anime-girl-hd-wallpaper-1080p",
  "ken-kaneki-wallpaper",
  "anna-shimoneta-wallpaper",
  "broly-wallpapers",
  "anime-succubus-wallpapers",
  "fullmetal-alchemist-brotherhood-wallpaper-hd",
  "dragon-ball-z-wallpaper",
  "dbz-wallpapers-hd-all-saiyans",
  "goku-kamehameha-wallpaper",
  "vegito-wallpapers-hd",
  "cute-anime-wallpapers-for-desktop",
  "noragami-iphone-wallpaper",
  "ssj4-vegeta-wallpaper",
  "dark-anime-girl-wallpaper",
  "akatsuki-no-yona-wallpaper",
  "naruto-wallpapers-hd-for-iphone",
  "mugen-samurai-champloo-wallpaper",
  "gangsta-anime-wallpapers-for-desktop",
  "mm-wallpaper",
  "vegeta-super-saiyan-god-wallpaper",
  "black-butler-wallpaper-hd",
  "majin-vegeta-wallpaper-hd",
  "touka-tokyo-ghoul-wallpaper",
  "tokyo-ghoul-rize-wallpaper",
  "vampire-knight-wallpaper",
  "dragon-ball-z-wallpaper-hd",
  "anime-live-wallpapers-for-desktop",
  "dark-anime-wallpaper-hd",
  "tokyo-ghoul-touka-wallpaper",
  "dragon-ball-z-bardock-wallpaper",
  "hd-anime-wallpapers-1080p",
  "4k-naruto-wallpaper",
  "pyrrha-nikos-wallpaper",
  "obito-wallpaper-hd",
  "gundam-wing-zero-wallpaper",
  "anime-halloween-wallpaper",
  "cowboy-bebop-backgrounds",
  "future-gohan-wallpaper",
  "uchiha-wallpaper-hd",
  "trigun-wallpaper",
  "top-anime-wallpapers",
  "dragon-ball-z-1080p-wallpaper",
  "epic-anime-wallpapers-hd",
  "cute-anime-chibi-wallpapers",
  "anime-christmas-wallpaper-hd",
  "uta-tokyo-ghoul-wallpaper",
  "dbz-wallpaper-goku-and-vegeta",
  "sword-art-online-hd-wallpaper",
  "albedo-overlord-wallpaper",
  "gaara-hd-wallpapers",
  "sinon-hd-wallpaper",
  "itachi-uchiha-wallpaper-hd",
  "minato-wallpaper-hd",
  "naruto-wallpaper-hd",
  "osomatsu-san-wallpaper",
  "spice-and-wolf-hd-wallpaper",
  "cute-anime-couple-wallpaper",
  "anime-wallpaper-and-screensavers",
  "persona-3-aigis-wallpaper",
  "badass-anime-wallpaper-1920x1080",
]

async def animepp():

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

@borg.on(admin_cmd(pattern="animedp ?(.*)"))

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

    await event.edit("**Starting Anime Profile Pics... **")
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
    "Anime DP": "`.animedp`"
    "\nUsage - Auto-changing dp of Anime Every 5 Mins(Default). \n\n"
    "`.animedp` <delay> <s or S for seconds, m or M for minute(s) Delay, h or H for hour(s) Delay and d or D for Day(s) Delay>"
    "\nUsage - Auto-changing dp of Anime with custom Delay. \n\n"
  }
)
