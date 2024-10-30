import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
#####
@dp.message(CommandStart())
async def cmd_start(message: Message): 
    await message.answer(message.from_user.full_name)

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда хелп')

@dp.message(F.text == 'Как дела рассказывай')
async def how_are_you(message: Message):
    await message.answer('ok')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer_photo(photo=message.photo[-1].file_id, caption=message.photo[-1].file_id)


@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMtZyEGXyC-Fvyo-zUCpMx1IqWpCQsAAjXiMRu1tQlJZwrHWjCca8wBAAMCAANzAAM2BA', caption='code my')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:    
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')