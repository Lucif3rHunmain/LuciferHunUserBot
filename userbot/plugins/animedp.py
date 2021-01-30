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
"rwby-blake-wallpaper", 
"anime-cat-girl-wallpaper", 
"anime-neko-wallpapers", 
"black-bullet-wallpaper-hd", 
"sasuke-wallpaper-hd", 
"angel-with-a-shotgun-wallpaper", 
"umbreon-and-espeon-wallpaper", 
"cute-anime-cat-wallpaper", 
"anime-boy-wallpaper-hd", 
"kakashi-hatake-wallpaper-hd", 
"tokyo-ghoul-wallpaper-hd", 
"animated-angel-wallpaper", 
"anime-glitter-force-wallpaper", 
"cute-anime-wallpaper-1920x1080", 
"akatsuki-cloud-wallpaper", 
"one-piece-chopper-wallpaper", 
"naruto-vs-sasuke-hd-wallpaper", 
"dbz-broly-wallpaper", 
"anime-hatsune-miku-wallpaper", 
"attack-on-titan-chibi-wallpaper", 
"typhlosion-wallpaper", 
"anime-wallpaper-for-phone", 
"tokyo-ghoul-kaneki-ken-wallpaper", 
"1440p-anime-wallpaper", 
"super-saiyan-god-goku-wallpaper", 
"groudon-vs-kyogre-wallpaper", 
"nerd-hello-kitty-wallpaper", 
"yu-gi-oh-wallpaper-exodia", 
"sasuke-uchiha-hd-wallpaper", 
"uchiha-symbol-wallpaper", 
"sharingan-wallpaper-hd-1920x1080", 
"2560-x-1080-anime-wallpaper", 
"mega-charizard-y-wallpaper", 
"anime-warrior-wallpaper", 
"voltron-hd-wallpaper", 
"anime-wallpaper-hd-1920x1080", 
"anime-fighting-wallpaper", 
"cute-eevee-evolutions-wallpaper", 
"2560-x-1440-wallpaper-anime", 
"female-anime-samurai-wallpaper", 
"cute-mlp-wallpapers", 
"kiznaiver-wallpaper", 
"4k-anime-wallpapers", 
"anime-wallpaper-1080x1920", 
"dragon-ball-gt-wallpaper-hd", 
"anime-desktop-wallpaper", 
"shisui-uchiha-wallpapers", 
"rock-lee-wallpaper", 
"anime-gamer-girl-wallpaper", 
"eren-and-levi-wallpaper", 
"aizen-wallpaper-hd", 
"dragon-ball-z-phone-wallpaper",
"frieza-wallpaper", 
"anime-fall-wallpapers", 
"levi-attack-on-titan-wallpaper", 
"sailor-moon-wallpaper-1920x1080", 
"anime-valentines-day-wallpaper", 
"eevee-wallpapers-for-computer", 
"anime-assassin-wallpaper", 
"neon-genesis-evangelion-wallpaper-hd", 
"anime-yuri-wallpaper", 
"anime-samurai-girl-wallpaper", 
"japanese-anime-wallpapers-manga", 
"sasuke-and-itachi-wallpaper-hd", 
"cowboy-bebop-wallpaper-1920x1080", 
"cowboy-bebop-swordfish-2560x1080-wallpapers", 
"samurai-champloo-wallpapers", 
"pikachu-wallpaper-1920x1080", 
"anime-wallpaper-1920x1080", 
"minimalist-anime-wallpapers", 
"cute-charmander-wallpapers", 
"anime-music-wallpaper", 
"kuroko-basketball-wallpaper", 
"anime-mermaid-wallpaper", 
"boruto-wallpaper-hd", 
"gundam-wing-wallpaper", 
"sword-art-online-2-wallpaper", 
"sao-wallpapers", 
"anime-android-wallpaper", 
"red-and-black-anime-wallpaper", 
"kaneki-tokyo-ghoul-wallpaper", 
"arpeggio-of-blue-steel-wallpaper", 
"naruto-nine-tails-wallpaper", 
"super-saiyan-2-gohan-wallpaper", 
"inuyasha-wallpaper-hd", 
"4k-anime-wallpaper", 
"yu-gi-oh-dark-magician-wallpaper", 
"jiraiya-wallpaper-hd", 
"high-quality-anime-wallpapers", 
"anime-vampire-girl-wallpaper", 
"sword-art-online-wallpaper-kirito", 
"anime-guy-wallpaper-hd", 
"anime-girl-hd-wallpaper-1080p", 
"ken-kaneki-wallpaper", 
"pikachu-wallpapers-for-computer", 
"broly-wallpapers", 
"anna-shimoneta-wallpaper", 
"anime-succubus-wallpapers", 
"fullmetal-alchemist-brotherhood-wallpaper-hd", 
"dragon-ball-z-wallpaper", 
"goku-kamehameha-wallpaper", 
"dbz-wallpapers-hd-all-saiyans",
"vegito-wallpapers-hd", 
"cute-anime-wallpapers-for-desktop", 
"noragami-iphone-wallpaper", 
"ssj4-vegeta-wallpaper", 
"mew-and-mewtwo-wallpaper", 
"dark-anime-girl-wallpaper", 
"eevee-evolution-wallpaper", 
"naruto-wallpapers-hd-for-iphone", 
"akatsuki-no-yona-wallpaper", 
"all-anime-characters-hd-wallpaper", 
"gangsta-anime-wallpapers-for-desktop", 
"vegeta-super-saiyan-god-wallpaper", 
"mugen-samurai-champloo-wallpaper", 
"mm-wallpaper", 
"ho-oh-and-lugia-wallpaper", 
"black-butler-wallpaper-hd", 
"umbreon-wallpaper", 
"majin-vegeta-wallpaper-hd", 
"vampire-knight-wallpaper", 
"tokyo-ghoul-rize-wallpaper", 
"touka-tokyo-ghoul-wallpaper", 
"anime-live-wallpapers-for-desktop", 
"dragon-ball-z-wallpaper-hd", 
"dark-anime-wallpaper-hd", 
"dragon-ball-z-bardock-wallpaper", 
"eevee-live-wallpaper", 
"tokyo-ghoul-touka-wallpaper", 
"robotech-wallpaper-hd", 
"4k-naruto-wallpaper", 
"hd-anime-wallpapers-1080p", 
"pyrrha-nikos-wallpaper", 
"gundam-wing-zero-wallpaper", 
"obito-wallpaper-hd", 
"anime-halloween-wallpaper", 
"cowboy-bebop-backgrounds", 
"one-piece-iphone-wallpaper", 
"anime-nature-wallpaper", 
"g1-transformers-wallpaper-hd", 
"future-gohan-wallpaper", 
"uchiha-wallpaper-hd", 
"trigun-wallpaper", 
"dragon-ball-z-1080p-wallpaper", 
"hetalia-nordics-wallpaper", 
"top-anime-wallpapers", 
"epic-anime-wallpapers-hd", 
"primal-groudon-and-kyogre-wallpaper", 
"jotaro-kujo-wallpaper", 
"cute-anime-chibi-wallpapers", 
"jojo-bizarre-adventure-wallpaper", 
"uta-tokyo-ghoul-wallpaper", 
"castle-in-the-sky-wallpaper", 
"anime-christmas-wallpaper-hd", 
"dbz-wallpaper-goku-and-vegeta", 
"spirited-away-wallpaper", 
"gundam-wing-deathscythe-wallpaper", 
"hellsing-ultimate-wallpaper", 
"albedo-overlord-wallpaper", 
"sword-art-online-hd-wallpaper", 
"hana-prison-school-wallpaper", 
"gundam-wing-wallpapers", 
"gengar-wallpaper-iphone", 
"my-little-pony-wallpaper-1920x1080", 
"pikachu-iphone-wallpaper", 
"rwby-nora-wallpaper", 
"pikachu-hd-wallpaper", 
"dragon-ball-iphone-wallpaper", 
"dragon-ball-z-piccolo-wallpaper", 
"mega-latios-wallpaper", 
"gaara-hd-wallpapers", 
"anime-forest-background", 
"sinon-hd-wallpaper", 
"bleach-ichigo-hollow-form-wallpaper", 
"anime-gun-wallpaper", 
"cool-anime-wolf-wallpapers", 
"anime-cherry-blossom-wallpaper", 
"minato-wallpaper-hd", 
"itachi-uchiha-wallpaper-hd", 
"unlimited-blade-works-wallpaper", 
"spice-and-wolf-hd-wallpaper", 
"osomatsu-san-wallpaper", 
"naruto-wallpaper-hd", 
"cute-anime-couple-wallpaper", 
"anime-wallpaper-and-screensavers", 
"persona-3-aigis-wallpaper", 
"badass-anime-wallpaper-1920x1080", 
"super-saiyan-god-hd-wallpaper", 
"madara-uchiha-wallpaper-hd", 
"rwby-neo-wallpaper", 
"anime-mecha-wallpaper", 
"sailor-moon-christmas-wallpaper", 
"goku-super-saiyan-4-wallpaper", 
"cowboy-bebop-phone-wallpaper", 
"gundam-unicorn-wallpaper-hd", 
"gurren-lagann-iphone-wallpaper", 
"gengar-wallpaper-hd", 
"mega-rayquaza-hd-wallpaper", 
"anime-gamer-girl-wallpapers", 
"log-horizon-wallpapers", 
"itachi-wallpapers-hd", 
"samurai-champloo-wallpaper-hd", 
"4k-dragon-ball-z-wallpaper", 
"eeveelutions-wallpaper-hd", 
"one-punch-man-wallpaper-hd", 
"jolteon-wallpaper-hd", 
"hd-noragami-wallpaper",
"nanatsu-no-taizai-wallpaper-hd", 
"shiny-mega-rayquaza-wallpaper", 
"gangsta-anime-wallpaper", 
"princess-mononoke-wallpaper-hd", 
"sad-anime-wallpaper", 
"scary-anime-wallpaper", 
"gundam-wing-wallpaper-hd", 
"noragami-aragoto-wallpaper", 
"ban-seven-deadly-sins-wallpaper", 
"dragon-ball-z-trunks-wallpaper", 
"hunter-x-hunter-hd-wallpaper", 
"noragami-wallpaper-iphone", 
"rwby-yang-wallpaper", 
"sasuke-uchiha-wallpapers-hd", 
"yoko-littner-wallpaper-hd", 
"killua-wallpaper-hd", 
"sailor-moon-hd-wallpaper-1920x1080", 
"erased-anime-wallpaper", 
"anime-wallpaper-3840x1080", 
"anime-scenery-wallpaper", 
"rwby-phone-wallpaper", 
"vegeta-hd-wallpapers", 
"rwby-desktop-wallpaper", 
"golden-frieza-wallpaper", 
"sailor-moon-crystal-hd-wallpaper", 
"cute-anime-wallpapers-hd", 
"assassination-classroom-wallpaper-hd", 
"akatsuki-log-horizon-wallpaper", 
"anime-dual-monitor-wallpaper", 
"funny-anime-wallpapers", 
"hunter-x-hunter-hisoka-wallpaper", 
"rurouni-kenshin-wallpaper-hd", 
"kawaii-anime-wallpaper", 
"super-sonico-wallpaper-hd", 
"dbz-hd-wallpaper-1920x1080", 
"anime-girl-warrior-wallpaper", 
"gundam-wallpaper-1920x1080", 
"erza-scarlet-wallpaper-hd", 
"rei-ayanami-wallpaper-hd", 
"steins-gate-wallpaper-hd", 
"japanese-animation-wallpaper", 
"creepy-anime-wallpaper", 
"howls-moving-castle-wallpaper", 
"anime-sniper-wallpaper", 
"one-punch-man-hd-wallpaper", 
"anime-panda-wallpaper", 
"super-saiyan-5-wallpaper", 
"jojos-bizarre-adventure-wallpaper-1920x1080", 
"hidden-leaf-village-wallpaper", 
"naruto-hd-wallpapers-1080p", 
"dragon-ball-super-wallpaper-hd"
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
