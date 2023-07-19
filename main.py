import requests, json
from pyshorteners import Shortener
from utils import printr,get_affiliate_url
from telethon.sync import TelegramClient
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
from telethon import TelegramClient,events,sync
from telethon import functions, types


# editable variables
API_ID = '20340026'    #Enter your Telegram app API ID
API_HASH = 'd1c2010562443ded33c1f4fa64f16bc4'  # Enter the created API Hash 
FROM_CHATS = [1315464303, 1491489500, 810184328, 1714047949,1450755585,980741307]
# TO_CHATS = -980741307
TO_CHATS = -810184328
# to_chat = -1629572275
AMAZON_AFFILIATE_ID = 'dualwarez-21'
# end


Bot = TelegramClient('telegram', API_ID, API_HASH)


Bot.start()
@Bot.on(events.NewMessage(chats=FROM_CHATS,incoming=True))
async def new_message_handler(event):
    is_amazon_link = False
    url = False


    printr("New message received!")
    print(event.message.message)
    

    # send compliment
    if event.chat_id == -810184328 or event.chat_id == -980741307:
        if event.message.message.lower()=="test":
            
            response_API = requests.get("https://complimentr.com/api")
            compliment= json.loads(response_API.text)['compliment']
            
            await event.respond(compliment)
            return
    # 
    

    initial_pointer = 0
    current_pointer = 0
    # contains_amazon_link = False
    for entity in event.message.entities:
        
        # print(entity)
        url_type = 'text'
        if isinstance(entity, MessageEntityUrl):
            url = event.message.raw_text[
                entity.offset : entity.offset + entity.length
            ]
            url_type='text'
            current_pointer = entity.offset + entity.length
        elif isinstance(entity, MessageEntityTextUrl):
            url = entity.url
            print(entity)
        else:
            continue

        # print(url)
        # print(entity)
        
        if url:
            long_url = requests.head(url, allow_redirects=True).url
            is_amazon_link = "https://www.amazon" in long_url

            # print(entity)
            
            if is_amazon_link:
                print(
                    event.message.raw_text[initial_pointer:entity.offset + entity.length]
                )
                # contains_amazon_link = True
                ""    

                # affiliate_url = get_affiliate_url(long_url,AMAZON_AFFILIATE_ID)
                # tiny_url = Shortener().tinyurl.short(affiliate_url)

                # message = event.message.text.replace(url, tiny_url)
                # event.message.text = message
    
    # if contains_amazon_link:
    # if is_amazon_link:
    #     printr("Sending updated message!")
    #     printr(event.message.message)
    #     await Bot.send_message(TO_CHATS, event.message)
    # else:
    #     printr("Cannot found amazon link.")


Bot.run_until_disconnected()