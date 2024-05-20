import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from config import database
from information import informaiton_router
from registration import registration_router
from start import start_router

load_dotenv('../.env')
TOKEN = getenv("MAHORAT_TOKEN")
dp = Dispatcher()


async def on_startup():
    database['users'] = database.get('users', {})


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.startup.register(on_startup)
    dp.include_routers(start_router, informaiton_router, registration_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# DOCKER START 717