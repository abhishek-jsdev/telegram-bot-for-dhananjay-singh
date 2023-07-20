import requests, json, re
from pyshorteners import Shortener
from telethon.sync import TelegramClient
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
from telethon import TelegramClient,events,sync
from telethon import functions, types


from strings import API_ID, API_HASH, FROM_CHATS, TO_CHATS, TEST_CHATS, AMAZON_AFFILIATE_ID
from utils import printr, get_affiliate_url, get_test_response


Bot = TelegramClient('telegram', API_ID, API_HASH)
saved_messages= []


Bot.start()
@Bot.on(events.NewMessage(chats=FROM_CHATS,incoming=True))
async def new_message_handler(event):
    
    is_amazon_link = False
    url = ''


    print("New message received!")
    # print(event.message.message)
    

    # send compliment to Test Channels
    if event.chat_id in TEST_CHATS:
        if event.message.message.lower() != 'test': return
        await event.respond(get_test_response())
        print("Test message send!")
        return
    # 


    start_pointer = 0
    end_pointer = 0
    non_amazon_contents=[]
    contains_amazon_link = False
    amazon_urls=[]
    

    for entity in event.message.entities:
                
        url_type = ''


        if isinstance(entity, MessageEntityUrl):
            url = event.message.raw_text[entity.offset : entity.offset + entity.length]
            url_type='text'

        elif isinstance(entity, MessageEntityTextUrl):
            url = entity.url
        
        else:
            continue

        end_pointer = entity.offset + entity.length
                
        
        if url:

            url = re.search("(?P<url>https?://[^\s]+)", url).group("url")            
            long_url = requests.head(url, allow_redirects=True).url
            is_amazon_link = "https://www.amazon" in long_url


            if is_amazon_link:

                contains_amazon_link = True
                affiliate_url = get_affiliate_url(long_url,AMAZON_AFFILIATE_ID)
                tiny_url = Shortener().tinyurl.short(affiliate_url)


                if 'text' in url_type:
                    amazon_urls.append([url,tiny_url])
                else:
                    entity.url = tiny_url

            else:
                non_amazon_contents.append(event.message.text[start_pointer:entity.offset + entity.length])


        start_pointer=end_pointer


    for au in amazon_urls:
        message = event.message.text.replace(au[0], au[1])
        event.message.text = message


    for content in non_amazon_contents:
        event.message.text = event.message.text.replace(content,"")


    if contains_amazon_link:

        print("Sending updated message!")
        # print(event.message.message)
        await Bot.send_message(TO_CHATS, event.message)

    else:
        printr("Cannot found amazon link.")


Bot.run_until_disconnected()