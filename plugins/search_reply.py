# plugins/search_reply.py

from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import os

# MongoDB connection
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://cinemashor0:RYRUL115JCOM47R4@myfilterbot.cdxakym.mongodb.net/?retryWrites=true&w=majority&appName=MyFilterBot")
client = MongoClient(MONGO_URL)
db = client["Myfilterbot"]   # Your DB name
collection = db["Telegram_files"]  # Your collection name

@Client.on_message(filters.text & filters.private)
async def keyword_search(client: Client, message: Message):
    text = message.text.strip().lower()

    # Ignore short messages
    if len(text) < 3:
        return

    # MongoDB search
    result = collection.find_one({"name": {"$regex": text, "$options": "i"}})

    if result:
        reply = f"**Movie:** {result['name']}\n**Link:** {result['link']}"
    else:
        reply = "Movie not found. Please check the spelling."

    await message.reply_text(reply)
