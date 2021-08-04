import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


class BigBrother(BaseMiddleware):
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
