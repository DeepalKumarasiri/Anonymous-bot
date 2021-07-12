from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("Hey! I am ANONYMOUS SENDER BOT.\n\n"
                 "Just Forward me some messages or media and I will anonymize the sender.\n\n"
                 "Please support the developer by joining the support channel.")
bottoken = Credentials.BOT_TOKEN
if bottoken != None:
    try:
        JEBotZ = TelegramClient("bot", 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(bot_token=Credentials.BOT_TOKEN)
    except Exception as e:
        print(f"ERROR!\n{str(e)}")
        print("Bot is quiting...")
        exit()
else:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()
   
if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("Visit our Movie Web Site","https://irupc.net/"),
                                         Button.url("Support Channel","https://t.me/iruPC")]])                                                                
    if event.message.media:
      try:
        cap = Credentials.CAPTION
        await client.send_file(event.chat.id, lel, caption=cap)
      except Exception:
        await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass

@JEBotZ.on(events.NewMessage(pattern="^/send ?(.*)"))
async def caption(event):
   if event.is_private:
        return
   a = await event.client.get_permissions(event.chat_id, event.sender_id)
   if a.is_admin:
      try:
        lel = await event.get_reply_message()
        cap = event.pattern_match.group(1)
        await JEBotZ.send_file(event.chat.id, lel, caption=cap)
      except Exception:
         await event.reply("Reply to a media file 🥴")
         return
   if not a.is_admin:
      await event.reply("Only admins can execute this command!")

@JEBotZ.on(events.NewMessage(pattern="^/send ?(.*)"))
async def caption(event):
   if event.is_group:
        return
   try:
     lel = await event.get_reply_message()
     cap = event.pattern_match.group(1)
     await JEBotZ.send_file(event.chat.id, lel, caption=cap)
   except Exception:
      await event.reply("Reply to a media file 🥴")
      return     

with client:
  client.run_until_disconnected() 
