from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice

from datetime import datetime
import logging

FORMAT = "[AADITYA] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
➻ ᴜsᴀɢᴇ:\n\n `/chatgpt` : Ask AnyThing.
    example: `/chatgpt Where is TajMahal?`

๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""
SOURCE = url=f"https://t.me/saikostar_xd"
UPDATE_CHNL = url=f"https://t.me/TH3ONLYCHANNEL"
DEVELOPER = url=f"https://t.me/sexyaaditya"
SOURCE_TEXT = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/sexyaaditya"),
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/TH3ONLYSUPPORT"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://t.me/saikostar_xd"),
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/TH3ONLYCHANNEL"),
    ],
]
X = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/sexyaaditya"),
        
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/TH3ONLYSUPPORT"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", 
                              url=f"https://t.me/TH3ONLYSUPPORT",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url=f"https://t.me/saikostar_xd")]])
HELP_READ = "➻ ᴜsᴇ /chatgpt write a simple flask app in python.  \n\n **➻ ᴜsᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ @sexyaaditya**"
HELP_BACK = [
     [
           InlineKeyboardButton(text="Qᴜᴇꜱᴛɪᴏɴ ᴛʜᴀᴛ ᴄʜᴀᴛɢᴘᴛ ᴄᴀɴ ꜱᴏʟᴠᴇ ", url=f"https://t.me/TH3ONLYCHANNEL"),
           
     ],
    [
           InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["","+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ριиgιиg..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ριиgιиg.....")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [Aaditya](https://t.me/sexyaaditya)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt Where is TajMahal?`")
        else:

            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2,
)

            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:    {e} ")


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @saikostar_xd
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @sexyaaditya
# github : @saikostar_xd
