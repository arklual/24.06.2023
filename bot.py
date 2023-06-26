from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, date
import zoneinfo
from strings import *
from settings import *

zone = zoneinfo.ZoneInfo("Europe/Moscow")
app = Client("bot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(posts_from_1))
async def on_new_message_1(client, message:Message):
    if date.today().weekday() > 4:
        return
    if datetime.now(zone).hour < 13 or datetime.now(zone).hour > 15:
        return
    text = ''
    file_id = None
    if message.text:
        text = message.text
    elif message.photo:
        if message.caption:
            text = message.caption
            file_id = message.photo.file_id
        else:
            await app.send_photo(send_to_1, message.photo.file_id)
            return
    if '15.00' in text.lower():
        await app.send_message(send_to_1, FT_MESSAGE)
        return
    elif 'брокер' in text.lower():
        await app.send_message(send_to_1, BROKER_MESSAGE)
        return
    elif '+' in text.lower():
        await app.send_photo(send_to_1, '/root/29.05.2023/a.jpg', caption='+')
        return
    else:
        if file_id:
            await app.send_photo(send_to_1, file_id, text)
        else:
            await app.send_message(send_to_1, text)

app.run()
