import time, os
from threading import Timer

# os.system("cls" if os.name == "nt" else "clear")
print(time.ctime(), "STARTING...")

from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
from utils import get_url_info

# Use your own values from my.telegram.org
api_id = 20340026
api_hash = "d1c2010562443ded33c1f4fa64f16bc4"
client = TelegramClient("anon", api_id, api_hash)
# affiliate_id='dualwarez-21' # add to utils.py file

# channels id that we want to recieve msgs from
channels_id = [1315464303, 1491489500, 810184328, 1714047949]
# our channel id where we want to forward msg
our_channel_id = -980741307

def start_bot():

    # listen for new message
    @client.on(events.NewMessage(chats=channels_id, incoming=True, forwards=False))
    async def new_message_handler(event):
        try:
            print(time.ctime(), "info:\n", "RECEIVED NEW MESSAGE...")

            is_amazon_link = True

            for entity in event.message.entities:
                message = event.message.text
                url = ""

                if isinstance(entity, MessageEntityUrl):
                    url = event.message.raw_text[
                        entity.offset : entity.offset + entity.length
                    ]
                if isinstance(entity, MessageEntityTextUrl):
                    url = entity.url

                if url:
                    # generate new affiliate url using tiny url api
                    url_info = get_url_info(url)
                    is_amazon_link = url_info["is_amazon_link"]
                    # replace url if it's a amazon link
                    if is_amazon_link:
                        new_message = message.replace(url, url_info["updated"])
                        event.message.text = new_message

            if is_amazon_link:
                print(time.ctime(), "info:\n", "SENDING MESSAGE...")
                await client.send_message(our_channel_id, event.message)
                print(time.ctime(), "info:\n", "MESSAGE SEND!")
            else:
                print(time.ctime(), "warn:\n", "NOT AN AMAZON LINK!")

        except Exception as error:
            print(time.ctime(), "error:")
            print("error:\n", error)
            print("event:\n", event)
            print("message:\n", event.message)
            pass

    
    with client:
        client.start()
        # client.run_until_disconnected()


def stop_bot():
    with client:
        client.disconnect()
        print(time.ctime(), "DISCONNECTING...")