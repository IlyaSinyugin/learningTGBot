import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


class BigBrother(BaseMiddleware):
    # 1
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("[---------------------New Update!---------------------]")
        logging.info("1. Pre Process Update")
        logging.info("Next point: Process Update")
        data["middleware_data"] = "This will go on until on_post_process_upadte"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        if user in banned_users:
            raise CancelHandler()

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2. Process update, {data=}")
        logging.info("Next point: Pre Process Message")

    # 3
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"3. Pre Process Message, {data=}")
        logging.info("Next Point: Filters, Process Message")
        data["middleware_data"] = "It will take place in on_process_message"

    # 4 Filters

    # 5
    async def on_process_message(self, message: types.Message, data: dict):
        logging.info(f"5. Process Message")
        logging.info("Next point: Handler")
        data["middleware_data"] = "This will go in Handler"

    # 6 Handler

    # 7
    async def on_post_process_message(self, message: types.Message, data_from_filter: list, data: dict):
        logging.info(f"7. Post Process Message, {data=}, {data_from_filter}")
        logging.info("Next point: Post Process Update")

    # 8
    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        logging.info(f"8. Post Process Update, {data=}, {data_from_handler=}")
        logging.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!The end!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")