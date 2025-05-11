# plugins/channel_filter.py

from pyrogram import Client, filters
from pyrogram.types import Message

CHANNEL_ID = -1001869198347  # ← Replace with your real channel ID

@Client.on_message(filters.text & filters.group)
async def filter_from_channel(client: Client, message: Message):
    keyword = message.text.strip().lower()

    if len(keyword) < 3:
        return

    async for msg in client.search_messages(chat_id=CHANNEL_ID, query=keyword, limit=1):
        try:
            await msg.copy(chat_id=message.chat.id, reply_to_message_id=message.message_id)
            return
        except:
            continue

    await message.reply_text("Kuch nahi mila, spelling check karo ya dusra keyword try karo.")
