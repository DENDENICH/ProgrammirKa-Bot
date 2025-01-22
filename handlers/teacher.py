from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import register_key


router_tch = Router()


# Состояния для работы с расписанием и домашней работой
class TeacherState(StatesGroup):
    waiting_for_schedule = State()
    waiting_for_homework = State()


@router_tch.message(Command("get_register_key"))
async def get_register_key(message: types.Message):
    key = register_key.generate_key()
    register_key.save_key(key) # сохранение ключа
    await message.answer(
        "Ключ для регистрации. Отправь его новому ученику!\n"
        f"```{key}```"
        )


# Хендлер для назначения домашнего задания
@router_tch.message(Command("set_homework"))
async def set_homework(message: types.Message):
    await message.answer("Введите домашнее задание для ученика.")
    await TeacherState.waiting_for_homework.set()


@router_tch.message(TeacherState.waiting_for_homework)
async def process_homework(message: types.Message, state: FSMContext):
    homework = message.text
    # TODO: Сохранить домашнее задание в базе данных
    await message.answer(f"Домашнее задание назначено: {homework}")
    await state.clear()

