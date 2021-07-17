from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "PROJECT GROUP", url="https://t.me/Nazriyaofftopic"
                    ),
                    InlineKeyboardButton("Project Channel", url="https://t.me/Nazriya_offtopic"),
                ],
                [InlineKeyboardButton("My Father", url="https://t.me/smile_killer_010")],
            ]
        ),
    )
