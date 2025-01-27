from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommandScopeChat

from config import bot, tg_config
from keywords.commands import teacher_command, student_command

basic_student_router = Router()


# command /start
@basic_student_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    """Start, set state for registration key"""
    if message.id in tg_config.admin_id: # is teacher

    else:
        bot.set_my_commands(
            commands=student_command,
            scope=BotCommandScopeChat(chat_id=message.chat.id),
        )
        await message.answer("Привет, ученик!")
