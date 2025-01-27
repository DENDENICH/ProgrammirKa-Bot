from aiogram import Router
from aiogram.filters import (
    Command,
)
from aiogram.types import Message

from utils.register_key import keys


register_teacher_router = Router()


@register_teacher_router.message(Command("get_new_key"))
async def generate_new_register_key(message: Message):
    """Handler for generate new unique auth key"""
    key = keys.generate_new_key()
    await message.answer(
        "Ключ для регистрации. Отправь его новому ученику!\n"
        f"```{key}```"
        )


@register_teacher_router.message(Command("get_all_keys"))
async def get_register_keys(message: Message):
    """Handler for get all saved auth keys"""
    keys_list = keys.get_all_keys()
    await message.answer(
        "Список сохраненных ключей:\n"
        f"```{keys}```".format(keys="\n".join(keys_list))
    )
