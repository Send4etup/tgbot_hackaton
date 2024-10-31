from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message): 
    await message.reply(message.from_user.full_name, 
                         reply_markup=await kb.inline_cars()),

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда хелп')

@router.message(F.text == 'Как дела рассказывай')
async def how_are_you(message: Message):
    await message.answer('ok')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer_photo(photo=message.photo[-1].file_id, caption=message.photo[-1].file_id)

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMtZyEGXyC-Fvyo-zUCpMx1IqWpCQsAAjXiMRu1tQlJZwrHWjCca8wBAAMCAANzAAM2BA', caption='code my')