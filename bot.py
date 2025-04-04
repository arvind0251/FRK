import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# 🔥 Bot Token (BotFather se lo)
TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🎯 Normal bot responses
responses = [
    "Hello! 😊", "Kaise ho? 😃", "Aaj ka din kaisa ja raha hai? 🔥",
    "Kya chal raha hai?", "Masti kar rahe ho kya?", "Khaana khaya?",
    "Aaj mausam kaise hai?", "Coding kar rahe ho?", "Kya plan hai aaj ka?"
]

@dp.message()
async def handle_message(message: Message):
    reply = random.choice(responses)  # 🔥 Random reply dega
    await message.reply(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
