import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the terminal
clear_terminal()

# import logging
# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

from telethon import TelegramClient, events, errors
from telethon.tl.types import MessageEntityTextUrl,MessageEntityUrl, PeerChannel

# Use your own values from my.telegram.org
api_id=20340026
api_hash='d1c2010562443ded33c1f4fa64f16bc4'
client = TelegramClient('anon',api_id,api_hash)

channels_id = {'offerzone':1315464303,'amazon':1491489500}

import requests
import urllib.parse

def expand_short_url(short_url):
    response = requests.head(short_url, allow_redirects=True)
    return response.url

# listen for new message
@client.on(events.NewMessage(chats = [1315464303,1491489500,810184328],incoming=True))
async def new_message_handler(event):
    try:
        # chat = await event.get_chat()
        # print('chat: ',chat)    
        # message=event.message.text
        # print('message: \n',message)   
        # raw_message=event.message.raw_text
        # print('raw message: \n',raw_message)  
        # entities=event.message.entities
        # print('entities: \n',entities)
        for entity in event.message.entities:
            message=event.message.text
            if isinstance(entity,MessageEntityUrl):
                # get url
                url = message[entity.offset:entity.offset+entity.length]

                long_url = expand_short_url(url)
                # print(long_url)
                # replace url
                # new_message=message.replace(url,'https://www.youtube.com/')
                new_message=message.replace(url,long_url)
                event.message.text=new_message
                
                # print(event.message.text)
            if isinstance(entity,MessageEntityTextUrl):
                # get url
                # url = message[entity.offset:entity.offset+entity.length]
                long_url = expand_short_url(entity.url)
                # print(long_url)
                # replace url
                # new_message=message.replace(entity.url,'https://www.youtube.com/')
                new_message=message.replace(entity.url,long_url)
                event.message.text=new_message
                # replace url
                # entity.url=await unshorten_url(entity.url)
                
        print(event.message.text)
        for entity in event.message.entities:
            print(entity)



        # message = event.message.message
        # peer_id = event.message.peer_id
        # entities = event.message.entities

        # if isinstance(peer_id,PeerChannel):
        #     for entity in entities:
        #         if isinstance(entity,MessageEntityTextUrl):
        #             # entity.url = await new_entity_url(entity.url)
        #             print()

        # with open("logs.txt", "a") as f:
        #     # dict={'event':event,'message':message,'entities':entities,'peer_id':peer_id}
        #     # print(dict, file=f)
        #     print('event::',event, file=f)
        #     print('message::',message, file=f)
        #     print('raw text::',event.raw_text,file=f)
        #     print('entities::',entities, file=f)
        #     print('peer_id::',peer_id, file=f)
        #     print('',file=f)

        # print(peer_id,message)
    except:
        print('error occured')
        pass

client.start()
client.run_until_disconnected()

# 23
