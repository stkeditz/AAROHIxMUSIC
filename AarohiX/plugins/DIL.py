from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

DIL = [" 🥺**🍃ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴅᴏsᴇɴ'ᴛ ɴᴇᴇᴅ ᴄᴜᴛᴇ ᴠᴏɪᴄᴇ ᴀɴᴅ ʟᴏᴠᴇʟʏ ғᴀᴄᴇ...🥺
 ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ɴᴇᴇᴅs ᴘᴜʀᴇ ʜᴇᴀʀᴛ ᴡɪᴛʜ ᴜɴʙʀᴇᴀᴋᴀʙʟᴇ ᴛʀᴜsᴛ🥀...🍃** "]

# Command
DIL_COMMAND = get_command("DIL_COMMAND")

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨sᴜᴘᴘᴏʀᴛ✨", url=f"https://t.me/LOVE_FEELINGS_WILL1"),
                    InlineKeyboardButton(
                        "✨ᴏᴡɴᴇʀ✨", url=f"https://t.me/HONEY_SINGH_121")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨sᴜᴘᴘᴏʀᴛ✨", url=f"https://t.me/LOVE_FEELINGS_WILL1"),
                    InlineKeyboardButton(
                        "✨ᴏᴡɴᴇʀ✨", url=f"https://t.me/HONEY_SINGH_121")
                    
                ]
            ]
        ),
    )
