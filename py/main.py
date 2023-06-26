from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id=20340026
api_hash='d1c2010562443ded33c1f4fa64f16bc4'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon',api_id,api_hash) as client:
    client.loop.run_until_complete(client.send_message('me','Hello, myself!'))