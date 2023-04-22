import time

from AarohiX import Update
from AarohiX.ext import CallbackContext, run_async

from AarohiX import dispatcher,OWNER_ID
from AarohiX.modules.disable import DisableAbleCommandHandler
from AarohiX.modules.helper_funcs.chat_status import user_admin

# sleep how many times after each edit in 'love'
EDIT_SLEEP = 1
# edit how many times in 'love'
EDIT_TIMES = 35

love_siren = [
    "😀",
    "👩‍🎨",
    "😁",
    "😂",
    "🤣",
    "😃",
    "😄",
    "😅",
    "😊",
    "☺",
    "🙂",
    "🤔",
    "🤨",
    "😐",
    "😑",
    "😶",
    "😣",
    "😥",
    "😮",
    "🤐",
    "😯",
    "😴",
    "😔",
    "😕",
    "☹",
    "🙁",
    "😖",
    "😞",
    "😟",
    "😢",
    "😭",
    "🤯",
    "💔",
    "❤",
    "I Love You❤",
]




@user_admin
@run_async
def love(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("Wait For Magic")
    for x in range(EDIT_TIMES):
        msg.edit_text(love_siren[x % 35])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("True Love💞")




LOVE_HANDLER = DisableAbleCommandHandler("love", love)
dispatcher.add_handler(LOVE_HANDLER)

__help__ = """

 ©️ [Anand] (f"tg://user?id={OWNER_ID}"))

*ғᴀᴋᴇ ᴀɴɪᴍᴀᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅ*
 ❍ /love - ᴜsᴇ ɪᴛ ɪғ ᴜ ʜᴀᴠᴇ ɢɪʀʟғʀɪᴇɴᴅ
 ❍ ʙʏ OWNER
"""
__mod_name__ = "♦️ ɢᴀᴍᴇ ♦️"
