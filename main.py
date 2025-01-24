from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage

from redis.asyncio import Redis

from config import tg_config


async def main() -> None:

    # set redis storage for FSM
    redis = Redis(host="localhost")
    storage = RedisStorage(redis=redis)

    # initialize bot and he config
    bot = Bot(token=tg_config.token)
    dp = Dispatcher(storage=storage)

    # TODO: инициализация и регистрация роутеров
