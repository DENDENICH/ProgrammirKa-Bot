from aiogram import (
    Router,
    types,
    F
)
from aiogram.filters import (
    Command,
    CommandStart,
    StateFilter
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import register_key
from filters import register_filter

from schemas import StudentModel


basic_student_router = Router()


# command /start
@basic_student_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    """Start, set state for registration key"""
    # TODO: сделать приветсвенное сообщение для вывода
    await message.answer("Привет, дорогой ученик!")
