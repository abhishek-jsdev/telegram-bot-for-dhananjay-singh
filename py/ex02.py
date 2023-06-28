import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# # Call the function to clear the terminal
# clear_terminal()

# import logging
# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

from telethon import TelegramClient, events, errors
from telethon.tl.types import MessageEntityTextUrl,MessageEntityUrl, PeerChannel

# Use your own values from my.telegram.org
api_id=20340026
api_hash='d1c2010562443ded33c1f4fa64f16bc4'
client = TelegramClient('anon',api_id,api_hash)
affiliate_id='dualwarez-21'
log_count=0

channels_id = {'offerzone':1315464303,'amazon':1491489500}

import requests
import urllib.parse

def expand_short_url(short_url):
    response = requests.head(short_url, allow_redirects=True)
    return response.url

def is_amazon_link(url):
    if 'https://www.amazon.in' in url:
        return True
    return False

# from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import urllib.parse

import re
def update_amazon_link(long_url):
    # url_parts = urllib.parse.urlparse(long_url)
    # query = dict(urllib.parse.parse_qs(url_parts.query))
    
    # amazon_url_params={'tag':[affiliate_id],'ref':'','red':'','ref_':''}

    # query.update(amazon_url_params)
    # url_parts[4] = urllib.parse.urlencode(query)
    # new_url = urllib.parse.urlunparse(url_parts)

    # print(new_url)

    # # print(query_params.get('tag'))
    # if query_params.get('tag'):
    #     del query_params['tag']
    #     query_params['tag'] = [affiliate_id]
    # else:
    #     query_params['tag'] = [affiliate_id]

    # if query_params.get('ref'):
    #     del query_params['ref']
    # if query_params.get('ref_'):
    #     del query_params['ref_']
    # if query_params.get('red'):
    #     del query_params['red']
    #     # query_params.tag[0]=[affiliate_id]

    # Update query parameters with new values
    # import urllib.parse

    # url = "http://stackoverflow.com/search?q=question"
    # params = {'lang':'en','tag':'python'}

    # url_parts = urllib.parse.urlparse(url)
    # query = dict(urllib.parse.parse_qsl(url_parts.query))
    # query.update(params)

    # new_url = url_parts._replace(query=urllib.parse.urlencode(query)).geturl()

    # print(query_params)
    # print(long_url)
    # print(updated_url)
    # return updated_url
    
    # start=re.match('tag=',long_url)
    # print(re.search('tag=', long_url))
    print(long_url)
    # long_url_parts = long_url.split('?')
    # long_url_arr = long_url_parts[0] + long_url_parts[1].split('&')
    # print(long_url_arr)

    # long_url_arr.extend()
    # long_url_arr = re.split("&|?",long_url)
    # print(long_url_arr)
    # print(long_url[long_url.rfind('tag=')+4:])
    # long_url = long_url+'&'
    # if re.search('tag=', long_url):
    #     pattern = r'tag=(.*?)&'
    #     replaced_string = re.sub(pattern, affiliate_id,long_url)
    # else:
    #     replaced_string = long_url+'&tag='+affiliate_id    
    # print('re: ',replaced_string)
    # return replaced_string

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
                url = message[entity.offset:entity.offset+entity.length]
                long_url = expand_short_url(url)
                if is_amazon_link(long_url):
                    update_amazon_link(long_url)
                    # replace url
                    # new_message=message.replace(url,'https://www.youtube.com/')
                    new_message=message.replace(url,long_url)
                    event.message.text=new_message
                
                    # print(event.message.text)
            if isinstance(entity,MessageEntityTextUrl):
                # get url
                # url = message[entity.offset:entity.offset+entity.length]
                long_url = expand_short_url(entity.url)
                if is_amazon_link(long_url):
                    update_amazon_link(long_url)
                    # print(long_url)
                    # replace url
                    # new_message=message.replace(entity.url,'https://www.youtube.com/')
                    new_message=message.replace(entity.url,long_url)
                    event.message.text=new_message
                    # replace url
                    # entity.url=await unshorten_url(entity.url)
                
        # print(event.message.text)
        # for entity in event.message.entities:
        #     print(entity)



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

    # finally:
    #     if log_count>10:
    #         clear_terminal()
    #         log_count=0
    #     else:
    #         log_count +=1

async def send_message():
    client

client.start()
client.run_until_disconnected()

# 23
