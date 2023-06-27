# import logging
# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

import urlexpander
from telethon import TelegramClient, events, errors
from telethon.tl.types import MessageEntityTextUrl, PeerChannel

# Use your own values from my.telegram.org
api_id=20340026
api_hash='d1c2010562443ded33c1f4fa64f16bc4'
client = TelegramClient('anon',api_id,api_hash)

channels_id = {'offerzone':1315464303,'amazon':1491489500}

async def unshorten_url(url):
    return await urlexpander.expand(url)

async def new_entity_url(url):
    long_url = unshorten_url(url)
    print(long_url)
    return url

# listen for new message
@client.on(events.NewMessage)
async def new_message_handler(event):
    try:
        message = event.message.message
        peer_id = event.message.peer_id
        entities = event.message.entities

        if isinstance(peer_id,PeerChannel):
            for entity in entities:
                if isinstance(entity,MessageEntityTextUrl):
                    # entity.url = await new_entity_url(entity.url)
                    print()

        with open("logs.txt", "a") as f:
            dict={'event':event,'message':message,'entities':entities,'peer_id':peer_id}
            print(dict, file=f)
            print()

        # print(peer_id,message)
    except:
        pass

client.start()
client.run_until_disconnected()
