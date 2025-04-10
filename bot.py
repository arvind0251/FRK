import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# 🔥 Bot Token (BotFather se lo)
TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🎯 Massive Keyword-Based Responses  
custom_replies = {
    "hello": ["Hello! 😊", "Hi there! 👋", "Hey! How are you?", "Salaam! 😃", "Namaste! 🙏"],
    "hi": ["Hi! 😃", "Hello! How’s your day?", "Hey there! 👋", "Hiiiii! 😍"],
    "kaise ho": ["Main badhiya! Tum sunao? 😃", "Ek dum mast! Aur tum?", "Zinda hoon, tum kaise ho?", "Life mast chal rahi hai!"],
    "kya kar rahe ho": ["Bas tumse baat kar raha hoon! 🤖", "Coding chal rahi hai! 💻", "Masti kar raha hoon! 😂", "Kuch nahi, bas timepass!"],
    "rudra": ["Rudra se baat kar rahe ho? 😎", "Rudra kaise hain? 🤔", "Rudra ek dum OP banda hai! 🔥", "Rudra is the legend! 🏆"],
    "Frk": ["Bidi Master 😅",""],
    "bye": ["Bye bye! 👋", "Phir milenge! 😊", "Take care! ❤️", "Goodbye, dost! 😢"],
    "masti": ["Masti toh full on chal rahi hai! 😆", "Masti time! 🕺", "Kabhi kabhi serious bhi ho jao! 😂"],
    "joke": ["Ek joke suno: Tera dimaag aur WiFi dono slow hai! 😂", "Ek aur joke? Tera face dekh ke bhi hansna aata hai! 😜"],
    "love": ["Pyaar mohabbat dosti sab bakwaas hai! 😂", "Dil se dil tak! ❤️", "Tumhara dil kitna bada hai? 💕"],
    "crush": ["Apna crush batao! 😍", "Koi pasand hai kya? 👀", "Crush se baat kar lo warna regret hoga! 😜"],
    "food": ["Khaana khaaya? 🍕", "Kya pasand hai tumhe? 🍔", "Biryani ya pizza? 🤔"],
    "mood": ["Kaisa mood hai? 😃", "Aaj khush lag rahe ho! 🔥", "Tension mat lo, sab theek hoga! 💪"],
    "movie": ["Konsi movie dekh rahe ho? 🎬", "Movie night plan hai kya? 🍿", "Horror movie pasand hai ya comedy? 😂"],
    "music": ["Kaunsa song sun rahe ho? 🎵", "Tumhara favourite singer kaun hai? 🎤", "Music bina life boring hai!"],
    "study": ["Padhai kar rahe ho? 📚", "Exam ka tension mat lo! 😎", "Smart study karo, hard work se better!"],
    "gaming": ["PUBG ya Free Fire? 🎮", "Gaming OP hai! 🔥", "Tumhara favourite game kaunsa hai?"],
    "cricket": ["IPL kaunsa team pasand hai? 🏏", "Cricket dekh rahe ho kya?", "Virat Kohli ya MS Dhoni?"],
    "weather": ["Mausam kaisa hai? 🌤️", "Aaj barish ho rahi hai kya? ☔", "Garmee lag rahi hai ya thand? ❄️"],
    "whatsapp": ["WhatsApp pe busy ho kya? 📱", "WhatsApp status kya lagaya hai?", "WhatsApp DP OP honi chahiye! 😂"],
    "instagram": ["Instagram pe kya chal raha hai? 📸", "Reel viral ho gayi kya? 😂", "Instagram stories dekh raha hai?"],
    "sleep": ["Neend aa rahi hai kya? 😴", "Raat bhar jagoge kya? 🌙", "Jaldi so jao warna panda ban jaoge! 🐼"],
    "birthday": ["Happy Birthday! 🎉", "Birthday kab hai tumhara?", "Party kidhar hai? 🎂"],
    "goal": ["Life ka goal kya hai? 🎯", "Sapne poore karne hain ya sirf sochna hai?", "Hard work se sab kuch possible hai! 🔥"],
       # 🟡 Daily Use Words
    "haan": ["Haan bolo! 😃", "Haan ji? 🤔", "Haan bhai, kya scene hai?", "Bilkul! 👍"],
    "nahi": ["Nahi matlab nahi! 😜", "Kyun nahi? 🤨", "Arre, ek baar soch lo!", "Theek hai, mat karo! 🙄"],
    "acha": ["Acha, sahi baat hai! 🤔", "Acha? Matlab kya? 😃", "Acha suno! 😆"],
    "thik hai": ["Theek hai bhai! ✅", "Maan liya! 😜", "Ok done! 💯"],
    "chalo": ["Chalo chalo, kaam pe lago! 😂", "Kaha jaana hai? 🧐", "Chalo bhai, party karte hain! 🕺"],
    "ruk": ["Ruko zara, sabar karo! 😂", "Kyu? Kya baat hai? 🤔", "Ruko, ek minute!"],
    "suno": ["Haan sun raha hoon! 🎧", "Bolo bolo! 😃", "Kuch important hai kya? 🤨"],
    "kab": ["Jab waqt aayega! ⏳", "Abhi nahi, thoda ruk jao! 😜", "Time batao toh sahi!"],
    "kyun": ["Bas aise hi! 😂", "Kyun matlab kyun? 🤔", "Tujhe kya lagta hai?"],
    "kaisa": ["Ek dum mast! 🔥", "Badiya! Tum sunao? 😃", "Life mast chal rahi hai!"],
    "kaun": ["Main hoon na! 😆", "Kaun? Kaun bola? 👀", "Tera bhai! 😂"],
    "kya": ["Kya matlab? 🤨", "Kya chahiye bhai? 😜", "Kya baat hai?"],
    
    # 🟠 Masti & Fun
    "masti": ["Masti toh full on chal rahi hai! 😆", "Masti time! 🕺", "Kabhi kabhi serious bhi ho jao! 😂"],
    "joke": ["Ek joke suno: Tera dimaag aur WiFi dono slow hai! 😂", "Ek aur joke? Tera face dekh ke bhi hansna aata hai! 😜"],
    "love": ["Pyaar mohabbat dosti sab bakwaas hai! 😂", "Dil se dil tak! ❤️", "Tumhara dil kitna bada hai? 💕"],
    "crush": ["Apna crush batao! 😍", "Koi pasand hai kya? 👀", "Crush se baat kar lo warna regret hoga! 😜"],
    
    # 🔵 Daily Life
    "food": ["Khaana khaaya? 🍕", "Kya pasand hai tumhe? 🍔", "Biryani ya pizza? 🤔"],
    "mood": ["Kaisa mood hai? 😃", "Aaj khush lag rahe ho! 🔥", "Tension mat lo, sab theek hoga! 💪"],
    "movie": ["Konsi movie dekh rahe ho? 🎬", "Movie night plan hai kya? 🍿", "Horror movie pasand hai ya comedy? 😂"],
    "music": ["Kaunsa song sun rahe ho? 🎵", "Tumhara favourite singer kaun hai? 🎤", "Music bina life boring hai!"],
    "study": ["Padhai kar rahe ho? 📚", "Exam ka tension mat lo! 😎", "Smart study karo, hard work se better!"],
    "gaming": ["PUBG ya Free Fire? 🎮", "Gaming OP hai! 🔥", "Tumhara favourite game kaunsa hai?"],
    "cricket": ["IPL kaunsa team pasand hai? 🏏", "Cricket dekh rahe ho kya?", "Virat Kohli ya MS Dhoni?"],
    "weather": ["Mausam kaisa hai? 🌤️", "Aaj barish ho rahi hai kya? ☔", "Garmee lag rahi hai ya thand? ❄️"],
    
    # 🟣 Social Media
    "whatsapp": ["WhatsApp pe busy ho kya? 📱", "WhatsApp status kya lagaya hai?", "WhatsApp DP OP honi chahiye! 😂"],
    "instagram": ["Instagram pe kya chal raha hai? 📸", "Reel viral ho gayi kya? 😂", "Instagram stories dekh raha hai?"],
    
    # 🔴 Night Chat
    "sleep": ["Neend aa rahi hai kya? 😴", "Raat bhar jagoge kya? 🌙", "Jaldi so jao warna panda ban jaoge! 🐼"],
    "birthday": ["Happy Birthday! 🎉", "Birthday kab hai tumhara?", "Party kidhar hai? 🎂"],
    
    # 🟢 Life Goals
    "goal": ["Life ka goal kya hai? 🎯", "Sapne poore karne hain ya sirf sochna hai?", "Hard work se sab kuch possible hai! 🔥"],
}


@dp.message()
async def handle_message(message: Message):
    reply = random.choice(responses)  # 🔥 Random reply dega
    await message.reply(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
