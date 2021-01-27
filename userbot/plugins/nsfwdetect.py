# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# ported to dc by @Lucif3rHun

import os
import requests
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, edit_delete, admin_cmd
from userbot.uniborgConfig import Config

DEEP_AI = os.environ.get("DEEP_AI", None)
@borg.on(admin_cmd(pattern="detect$", outgoing=True))
async def detect(event):
    if Config.DEEP_AI is None:
        return await edit_delete(
            event, "Add VAR `DEEP_AI` get Api Key from https://deepai.org/", 5
        )
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "`Reply to any image or non animated sticker !`", 5
        )
    catevent = await edit_or_reply(event, "`Downloading the file to check...`")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await edit_delete(
            event, "`Reply to any image or non animated sticker !`", 5
        )
    catevent = await edit_or_reply(event, "`Detecting NSFW limit...`")
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": Config.DEEP_AI},
    )
    os.remove(media)
    if "status" in r.json():
        return await edit_delete(catevent, r.json()["status"])
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    detections = r_json["detections"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"<b>Detected Nudity :</b>\n<a href='{link}'>>>></a> <code>{percentage:.3f}%</code>\n\n"
    if detections:
        for parts in detections:
            name = parts["name"]
            confidence = int(float(parts["confidence"]) * 100)
            result += f"<b>• {name}:</b>\n   <code>{confidence} %</code>\n"
    await edit_or_reply(
        catevent,
        result,
        link_preview=False,
        parse_mode="HTML",
    )
CMD_HELP.update(
    {
        "nsfwdetect": ".detect"
        "\nUsage: Reply .detect command to any image or non animated sticker to detect the nudity in that\n\n"
    }
)
