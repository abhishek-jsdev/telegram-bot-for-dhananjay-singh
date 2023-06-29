# import logging
# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

from telethon import TelegramClient, events, errors
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl, PeerChannel
from utils import get_url_info

# Use your own values from my.telegram.org
api_id = 20340026
api_hash = "d1c2010562443ded33c1f4fa64f16bc4"
client = TelegramClient("anon", api_id, api_hash)
# affiliate_id='dualwarez-21'

# channels id that we want to recieve msgs from
# channels_id = {'offerzone':1315464303,'amazon':1491489500,'test':810184328}
channels_id = [1315464303, 1491489500, 810184328, 1714047949]
# our channel id where we want to forward msg
our_channel_id = -980741307


# listen for new message
@client.on(events.NewMessage(chats=channels_id, incoming=True, forwards=False))
async def new_message_handler(event):
    try:
        print('RECEIVED NEW MESSAGE...')
        
        is_amazon_link = True

        for entity in event.message.entities:
            message = event.message.text

            url = None

            if isinstance(entity, MessageEntityUrl):
                url = message[entity.offset : entity.offset + entity.length]
            elif isinstance(entity, MessageEntityTextUrl):
                url = entity.url
            
            if url:
                # generate new tiny affiliate url
                url_info = get_url_info(url)
                is_amazon_link = url_info["is_amazon_link"]
                # replace url if it's a amazon link
                if is_amazon_link:
                    new_message = message.replace(url, url_info["updated"])
                    event.message.text = new_message

        if is_amazon_link:
            print("SENDING MESSAGE...")
            await client.send_message(our_channel_id, event.message)
            print("MESSAGE SEND!")
        else:
            print("NOT AN AMAZON LINK!")

    except Exception as error:
        print(error)
        pass


with client:
    client.start()
    client.run_until_disconnected()
