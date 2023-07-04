#    Copyright (c) 2021 Ayush
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
from utils import parse_url

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION_STRING = config("SESSION_STRING")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")
AMAZON_AFFILIATE_ID = config("AMAZON_AFFILIATE_ID")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    Bot = TelegramClient(SESSION_STRING, APP_ID, API_HASH)
    Bot.start()
except Exception as exception:
    print(f"ERROR - {exception}")
    exit(1)


@Bot.on(events.NewMessage(incoming=True, chats=FROM, forwards=True))
async def massage_handler(event):
    try:
        is_amazon_link = False
        url = False

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
                parsed_url = parse_url(url, AMAZON_AFFILIATE_ID)
                is_amazon_link = parsed_url["is_amazon_link"]

                if is_amazon_link:
                    message = event.message.text.replace(url, parsed_url["updated"])
                    event.message.text = message

        if is_amazon_link:
            for channel in TO:
                try:
                    await Bot.send_message(channel, event.message)
                except Exception as e:
                    print(e)
        else:
            # warning("Cannot found amazon link.")
            print("Cannot found amazon link.")

    except Exception as exception:
        # error({"message": event.message, "event": event, "error": exception})
        print(
            "message: ",
            event.message,
            "\n",
            "event: ",
            event,
            "\n",
            "error: ",
            exception,
        )
        print("Error occured! Check logs for more.")
        pass


print("Bot has started.")
Bot.run_until_disconnected()
