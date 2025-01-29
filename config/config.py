from environs import Env

from redis.asyncio import Redis

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage


env = Env
env.read_env()


class TGConfig:
    token: str = env('token')
    token_ai: str = env('token_ai')
    admin_id: int = int(env('admin_id'))


# set redis storage for FSM
_redis = Redis(host="localhost")
_storage = RedisStorage(redis=_redis)

tg_config = TGConfig()

# initialize bot and he config
bot = Bot(token=tg_config.token)
dp = Dispatcher(storage=_storage)
