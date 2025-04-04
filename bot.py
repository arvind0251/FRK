import random  
from aiogram import Bot, Dispatcher, types  
from aiogram.types import Message  
import asyncio  

TOKEN = "8075167051:AAG2UxaxCcQJeUkni6Z0iI5YkMawxTLvI0U"  

bot = Bot(token=TOKEN)  
dp = Dispatcher()  

# Load responses  
with open("responses.txt", "r", encoding="utf-8") as f:  
    responses = f.readlines()  

# Load emojis  
with open("emojis.txt", "r", encoding="utf-8") as f:  
    emojis = f.read().split()  

# Load GIFs  
with open("gifs.txt", "r", encoding="utf-8") as f:  
    gifs = f.read().splitlines()  

@dp.message()  
async def handle_message(message: Message):  
    text_reply = random.choice(responses).strip()  
    emoji_reply = random.choice(emojis)  
    gif_reply = random.choice(gifs)  

    # 70% chance text + emoji, 30% chance GIF  
    if random.random() < 0.7:  
        final_reply = f"{text_reply} {emoji_reply}"  
        await message.reply(final_reply)  
    else:  
        await message.reply_animation(gif_reply)  # Sending GIF  

async def main():  
    await dp.start_polling(bot)  

if __name__ == "__main__":  
    asyncio.run(main())  
