from aiogram import types

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), user_id=[347526285], text="admin")
@dp.message_handler(IsPrivate(), user_id=[347526285], text="secret")
async def admin_chat_secret(message: types.Message):
    await message.answer("Secret message, called by an administrator in the personal chat")
