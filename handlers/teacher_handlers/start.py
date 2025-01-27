from aiogram import Router, F
from aiogram.types import Message, BotCommandScopeChat
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import parse_datetime
from keywords.commands import teacher_command
from config import tg_config, bot


# TODO: хендлер старт для отправки меню команд


start_teacher_router = Router()


@start_teacher_router.message(CommandStart(), lambda message: message.id in tg_config.admin_id)
async def start_teacher(message: Message):
    bot.set_my_commands(
        commands=teacher_command,
        scope=BotCommandScopeChat(chat_id=message.chat.id),
    )
    await message.answer("Привет, учитель!")