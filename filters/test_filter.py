import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data


class SomeF(BoundFilter):
    async def check(self, message: types.Message):
        data = ctx_data.get()
        logging.info(f"4. Filter, {data=}")
        logging.info("Next Point: Process Message")
        return {"from_filter": "Data from filter"}