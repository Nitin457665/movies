# plugins/better_filter.py

from pyrogram import Client, filters
from pyrogram.types import Message
import os

db = client["Myfilterbot"]
filters_collection = db["filters"]

# 1. Add Filter
@Client.on_message(filters.command("add") & filters.private)
async def add_filter(client, message: Message):
    try:
        _, keyword, reply = message.text.split(" ", 2)
    except:
        return await message.reply_text("Usage:\n`/add movie_name your reply text`")

    filters_collection.update_one(
        {"keyword": keyword.lower()},
        {"$set": {"reply": reply}},
        upsert=True
    )
    await message.reply_text(f"Filter for '{keyword}' added.")

# 2. Delete Filter
@Client.on_message(filters.command("del") & filters.private)
async def delete_filter(client, message: Message):
    try:
        _, keyword = message.text.split(" ", 1)
    except:
        return await message.reply_text("Usage:\n`/del movie_name`")

    result = filters_collection.delete_one({"keyword": keyword.lower()})
    if result.deleted_count:
        await message.reply_text(f"Deleted filter for '{keyword}'.")
    else:
        await message.reply_text("No such filter found.")

# 3. Auto Filter Handler
@Client.on_message(filters.text & filters.private)
async def filter_reply(client, message: Message):
    keyword = message.text.strip().lower()
    result = filters_collection.find_one({"keyword": keyword})

    if result:
        await message.reply_text(result["reply"])
