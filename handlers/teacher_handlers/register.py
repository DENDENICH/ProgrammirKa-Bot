from aiogram import (
    Router,
    F
)
from aiogram.filters import (
    Command,
    CommandStart,
    StateFilter
)
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import register_key


register_teacher_router = Router()


@register_teacher_router.message(Command("get_register_key"))
async def get_register_key(message: Message):
    """Handler for generate unique auth key"""
    key = register_key.generate_key()
    register_key.save_key(key) # сохранение ключа
    await message.answer(
        "Ключ для регистрации. Отправь его новому ученику!\n"
        f"```{key}```"
        )
