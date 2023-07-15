import os
import random
import time
import asyncio
import requests
import json
# import logging
# from keep_alive import keep_alive,run       #To keep the bot running 24*7


from utils import parse_url,printr,get_compliment
from telethon.sync import TelegramClient
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
from telethon import TelegramClient,events,sync
from telethon import functions, types


# logging.basicConfig(filename='logs.txt', format='%(asctime)s - %(levelname)s - %(message)s')

api_id = '20340026'    #Enter your Telegram app API ID
api_hash = 'd1c2010562443ded33c1f4fa64f16bc4'  # Enter the created API Hash 
from_chats = [1315464303, 1491489500, 810184328, 1714047949,1450755585,980741307]
to_chat = -980741307
# to_chat = -1629572275
amazon_affiliate_id = 'dualwarez-21'


Bot = TelegramClient('foxonfire', api_id, api_hash)


Bot.start()
@Bot.on(events.NewMessage(chats=from_chats,incoming=True))
async def message_handler(event):
    is_amazon_link = False
    url = False

    printr("New message received!")
    # printr(event.chat_id)
    printr(event.message.message)
    
    # if event.chat_id == -980741307:
    if event.chat_id == -810184328 or event.chat_id == -980741307:
        if event.message.message.lower()=="test":
            compliment = get_compliment()
            await event.respond(compliment)
            return
    
    for entity in event.message.entities:
        
        if isinstance(entity, MessageEntityUrl):
            url = event.message.raw_text[
                entity.offset : entity.offset + entity.length
            ]
        elif isinstance(entity, MessageEntityTextUrl):
            url = entity.url
        else:
            continue
        
        if url:
            parsed_url = parse_url(url, amazon_affiliate_id)
            is_amazon_link = parsed_url["is_amazon_link"]
            if is_amazon_link:
                message = event.message.text.replace(url, parsed_url["updated"])
                event.message.text = message
    
    if is_amazon_link:
        printr("Sending updated message!")
        printr(event.message.message)
        await Bot.send_message(to_chat, event.message)
    else:
        printr("Cannot found amazon link.")


# keep_alive()
# Bot.run_until_disconnected()

# async def is_bot_alive():
#     # while True:
#     if Bot.is_connected():
#         printr('bot is alive')
#     else:
#         printr('bot is dead')
#         printr('starting bot')
#         Bot.start()
#     await asyncio.sleep(60.0)
#     is_bot_alive()

#  wrap in Task object
# -> automatically attaches to event loop and executes
# async def main():
#     await asyncio.gather(Bot.run_until_disconnected(),is_bot_alive())
# asyncio.run(main())
Bot.run_until_disconnected()