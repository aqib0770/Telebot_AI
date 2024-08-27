from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import openai
import sys

class Reference:
    '''
    A class to store previous response from Open AI AI
    '''

    def __init__(self) -> None:
        self.response = ""

load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")

reference = Reference()
TOKEN = os.getenv("TOKEN")

MODEL_NAME = 'gpt-4o-mini'

bot = Bot(token=TOKEN)
dp = Dispatcher()
client = openai.OpenAI(api_key=os.getenv("OpenAI_API_KEY"))


def clear_past():
    '''
    A function to clear the previous conversations and context'''
    reference.response = ""

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
    Hi, I am telegram bot powered by Open AI created by Aqib. Please follow these commands\n
    /start - to start the conversation\n
    /clear - to clear the past conversation and context\n
    /help - to get this help menu
    I hope this helps you. 
    """
    await message.reply(help_command)


@dp.message()
async def chatgpt(message: types.Message):
    print(f">>>USER: \n\t{message.text}")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content":reference.response},
            {"role": "user", "content": message.text}
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())