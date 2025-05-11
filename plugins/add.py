# plugins/add.py

from pyrogram import Client, filters
from pyrogram.types import Message
import os

# MongoDB setup from environment or hardcoded
db = client["Myfilterbot"]  # You can change this to match your DB name  # Collection name

# Only allow admins or specific users
ALLOWED_USERS = [5301956231]  # Replace with your Telegram user ID

@Client.on_message(filters.command("add") & filters.private)
async def add_movie(bot: Client, message: Message):
    if message.from_user.id not in ALLOWED_USERS:
        return await message.reply_text("Access denied.")

    try:
        cmd_parts = message.text.split(maxsplit=2)
        if len(cmd_parts) < 3:
            return await message.reply_text("Usage: /add <movie_name> <download_link>")

        name, link = cmd_parts[1], cmd_parts[2]

        collection.insert_one({"name": name, "link": link})
        await message.reply_text(f"Movie '{name}' added successfully!")

    except Exception as e:
        await message.reply_text(f"Error: {e}")
