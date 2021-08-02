import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 666666

    # doesn't get in error handler, deals with try
    try:
        await message.answer("Not correctly closed <b>tag<b>")
    except Exception as err:
        await message.answer(f"Not in error handler. Error: {err}")

    # doesn't get in error handler
    try:
        await bot.send_message(chat_id=non_existing_user, text="Non existing user")
    except Exception as err:
        await message.answer(f"Not in error handler. Error: {err}")

    # gets in error handler
    await message.answer("This <kek>tag</kek> doesn't exist")
    logging.info("This is not done, but bot won't be down.")

    await message.answer("...")