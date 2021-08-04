from aiogram import Dispatcher

from loader import dp
from .test_filter import SomeF

# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(SomeF)
