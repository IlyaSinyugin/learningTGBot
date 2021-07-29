import re

from aiogram import types
from aiogram.dispatcher.filters import CommandStart, ChatTypeFilter
from aiogram.utils.deep_linking import get_start_link

from loader import dp


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f"hello, {message.from_user.full_name}!\n"
                         f"You are in the personal chat\n"
                         f"You send an argument {deep_link_args}")

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.me
    deep_link = await get_start_link(payload="123")
    await message.answer(f"hello, {message.from_user.full_name}!\n"
                         f"You are in the personal chat\n"
                         f"Your command does not contain a deeplink\n"
                         f"Your deeplink is {deep_link}")