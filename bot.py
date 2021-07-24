import os
import time 
from telethon import TelegramClient 
from telethon import Buttons, events 
from config import config 

API_ID = config.API_ID
API_HASH = config.API_HASH
TOKEN = config.BOT_TOKEN 

hope = TelegramClient("hope", API_ID, API_HASH).start(bot_token=TOKEN)

@hope.on(events.NewMessage(pattern="/start"))
async def start(event):
     await event.reply("Hello! Welcome to the 𝐑𝐱𝐏𝐚𝐫𝐚𝐦𝐚𝐫𝐬𝐡!\nWith 𝐑𝐱𝐏𝐚𝐫𝐚𝐦𝐚𝐫𝐬𝐡! you can find out BOOKS, POSTS, HEALTH NEWS and\nSTUDY MATERIAL, UPDATES.\nPress Buttons to check out:", buttons=[
        [
          Button.url("Books", url="https://t.me/RxParamarsh/3684"),
          Button.url("Notes", url="https://t.me/RxParamarsh/3469"),
          Button.url("Videos", url="https://t.me/RxParamarsh/2673")
         ],
         [
          Button.url("My Pro Owner✨", url="https://t.me/Sthitpragya")
         ],
         [
           Button.inline("Next", data="nxt")]
           ])
@hope.on(events.callbackquery.CallbackQuery(data="nxt"))
async def nxt(event):
      await event.edit("NexT Page Check More by Clicking below:", buttons=[
        [
          Button.url("Drugs info", url="https://t.me/RxParamarsh/3880"),
          Button.url("PCI ACT", url="https://t.me/RxParamarsh/3881"),
          Button.url("Questions/Answer", url="https://t.me/RxParamarsh/3882"),
          Button.url("Pharm.D", url="https://t.me/RxParamarsh/3989")
        ],
        [
          Button.inline("Back", data="bck")],
          ])
          
@hope.on(events.callbackquery.CallbackQuery(data="bck"))
async def bck(event):
      await event.edit("Hello! Welcome to the 𝐑𝐱𝐏𝐚𝐫𝐚𝐦𝐚𝐫𝐬𝐡!\nWith 𝐑𝐱𝐏𝐚𝐫𝐚𝐦𝐚𝐫𝐬𝐡! you can find out BOOKS, POSTS, HEALTH NEWS and\nSTUDY MATERIAL, UPDATES.\nPress Buttons to check out:", buttons=[
        [
          Button.url("Books", url="https://t.me/RxParamarsh/3684"),
          Button.url("Notes", url="https://t.me/RxParamarsh/3469"),
          Button.url("Videos", url="https://t.me/RxParamarsh/2673")
        ],
        [
           Button.inline("Next", data="nxt")]
           ])
        
     
   
hope.run_until_disconnected()
# © Alone_loverboy
# For apna bhai (HOPE!)
# Personal hai kang maat karna😂😂
