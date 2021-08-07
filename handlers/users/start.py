import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.test_filter import SomeF
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, key="start")
@dp.message_handler(CommandStart(), SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter):
    await message.answer(f"Привет, {message.from_user.full_name}! \n{middleware_data=}\n{from_filter=}")
    logging.info(f"6. Handler")
    logging.info("Next point: Post Process Message")
    return {"from_handler": "Data from handler"}

