from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import register_key


router = Router()


# Состояния для регистрации учеников
class RegistrationState(StatesGroup):
    waiting_for_key = State()
    waiting_for_name = State()


# Хендлер для начала регистрации
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Введите ваш регистрационный ключ для начала.")
    await RegistrationState.waiting_for_key.set()


# Хендлер для проверки регистрационного ключа
@router.message(RegistrationState.waiting_for_key)
async def process_registration_key(message: types.Message, state: FSMContext):
    registration_key = message.text.strip()
    # TODO: Проверить ключ в базе данных
    valid_key = register_key.read_key().strip() # reading key from file

    if valid_key == register_key:
        await message.answer("Ключ подтвержден! Введите ваше имя.")
        register_key.delete_key() # delete exists key from file
        await RegistrationState.waiting_for_name.set()
    else:
        await message.answer("Неверный ключ. Попробуйте снова.")


# Хендлер для завершения регистрации
@router.message(RegistrationState.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    student_name = message.text
    # TODO: Сохранить данные в базе данных
    await message.answer(f"Регистрация завершена! Добро пожаловать, {student_name}.")
    await state.clear()


# Хендлер для вывода учебной программы ученика
@router.message(Command("program"))
async def show_study_program(message: types.Message):
    # TODO: Получить список учебной программы из базы данных
    study_program = "1. Основы Python\n2. Асинхронность\n3. Работа с базами данных"
    await message.answer(f"Ваша учебная программа:\n{study_program}")


# Хендлер для вывода домашнего задания
@router.message(Command("homework"))
async def show_homework(message: types.Message):
    # TODO: Получить домашнее задание из базы данных
    homework = "Изучить модули asyncio и написать простой пример."
    await message.answer(f"Ваше домашнее задание:\n{homework}")