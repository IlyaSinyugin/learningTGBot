from aiogram import Dispatcher
from .private_chat import IsPrivate
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)


