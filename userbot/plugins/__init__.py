import math
import os
import re
import time

import heroku3
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from userbot.uniborgConfig import config

# =================== CONSTANT ===================
USERID = bot.uid
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "legend"

# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"

PM_START = []

if config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = config.PRIVATE_GROUP_BOT_API_ID

# spamwatch support
if config.SPAMWATCH_API:
    token = config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None
