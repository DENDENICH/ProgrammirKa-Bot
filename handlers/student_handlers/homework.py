from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from data_base import data_base
from keywords.student import complete_homework


homework_student_router = Router()


# Хендлер для вывода домашнего задания
@homework_student_router.message(Command("homework"))
async def show_homework(message: Message):
    homework = await data_base.get_homework(tg_id=message.id)
    if homework.complete_homework:
        await message.answer(
                "Домашнее задание:"
                f"{homework.homework}",
                reply_markup=complete_homework
            )
    else:
        await message.answer(
                "Ты уже выполнил задание, ожидай нового :)"
            )
    

@homework_student_router.message(F.data == "complete_homework")
async def complete_homework(callback: CallbackQuery):
    data_base.complete_homework(tg_id=callback.chat.id)
    await callback.answer(
        "Молодец! Проверим задание на уроке ;)"
    )
