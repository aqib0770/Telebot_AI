import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv("TOKEN")
bot = Bot(token=api_token)
dp = Dispatcher()

@dp.message(Command('start'))
async def command_start(message: types.Message):
    await message.reply("Hello, I am your telegram bot")

@dp.message()
async def command_start(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())