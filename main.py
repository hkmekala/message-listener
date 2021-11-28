import logging
import os
from telethon import TelegramClient, events, sync
from playsound import playsound
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv('./.env')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage(chats='biscuit'))
async def my_event_handler(event):
    print(event.raw_text)
    playsound(os.path.abspath("./music_play.mp3"))

    try:
        myobj = gTTS(text=event.raw_text, lang='en', slow=False)
        myobj.save("./welcome.mp3")
        os.system("mpg321 welcome.mp3")
    except Exception as e:
        logging.error("Some Error from Text to Speech", e)


client.start()
client.run_until_disconnected()
