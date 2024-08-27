from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import google.generativeai as genai


class Reference:
    '''
    A class to store previous response from Gemini AI
    '''
    def __init__(self) -> None:
        self.history = []


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

GEMINI_API = os.getenv('GEMINI_AI_API_KEY')
genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel(model_name='gemini-1.0-pro-latest')

reference = Reference()


def clear_past():
    '''
    A function to clear the previous conversations and context
    '''
    reference.history = []


@dp.message(Command('start'))
async def welcome(message: types.Message):
    await message.reply("Hello, I am your telegram bot\nCreated by Aqib.\nHow may I assist you?")


@dp.message(Command('clear'))
async def clear(message: types.Message):
    clear_past()
    await message.reply("Past conversation and context has been cleared")


@dp.message(Command('help'))
async def helper(message: types.Message):
    help_command = """
    Hi, I am telegram bot powered by Open AI created by Aqib. Please follow these commands:

    /start - to start the conversation
    /clear - to clear the past conversation and context
    /help - to get this help menu

    I hope this helps you. 
    """
    await message.reply(help_command)


@dp.message()
async def gemini(message: types.Message):
    print(f">>>USER: \n\t{message.text}")
    
    reference.history.append({"role": "user", "parts": [message.text]})
    response = model.generate_content(reference.history)
    reference.history.append({"role": "model", "parts": [response.text]})
    
    print(f">>> GEMINI: \n\t{response.text}")
    await bot.send_message(chat_id=message.chat.id, text=response.text)
    
    reference.history = reference.history[-10:]


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())