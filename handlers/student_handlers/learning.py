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

from schemas import StudentModel


learning_student_router = Router()


# command /program
# This handler get description about learning program
@learning_student_router.message(Command("program"))
async def show_study_program(message: Message):
    # TODO: Получить список учебной программы из базы данных, с подробным описанием текущего этапа
    await message.answer(f"Ваша учебная программа:")


# Хендлер для вывода домашнего задания
@learning_student_router.message(Command("homework"))
async def show_homework(message: Message):
    # TODO: Получить домашнее задание из базы данных
    homework = "Изучить модули asyncio и написать простой пример."
    await message.answer(f"Ваше домашнее задание:\n{homework}")


@learning_student_router.message(Command("help_homework"))
async def help_homework(message: Message):
    # TODO: api с языковой моделью для помощи по домашней работе
    pass