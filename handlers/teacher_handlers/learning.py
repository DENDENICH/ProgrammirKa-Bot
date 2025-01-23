from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import register_key


learning_teacher_router = Router()


class ChooseStudentState(StatesGroup):
    """State for choose student"""
    choosing_student = State()

class TeacherState(StatesGroup):
    choosing_action = State()
    waiting_for_homework = State()
    waiting_for_schedule = State()


@learning_teacher_router.message(Command("get_register_key"))
async def get_register_key(message: Message):
    """Handler for generate unique auth key"""
    key = register_key.generate_key()
    register_key.save_key(key) # сохранение ключа
    await message.answer(
        "Ключ для регистрации. Отправь его новому ученику!\n"
        f"```{key}```"
        )


# Хендлер для выбора ученика
@learning_teacher_router.message(Command("manage_students"))
async def manage_students(message: types.Message):
    """Handler for choose student"""
    students = None # получение учеников из базы данных
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*students)
    await message.answer("Выберите ученика:", reply_markup=keyboard)
    await TeacherState.choosing_student.set()


@learning_teacher_router.message(TeacherState.choosing_student)
async def choose_student(message: types.Message, state: FSMContext):
    """Reading choose student for edit his data"""
    selected_student = message.text.strip()
    # TODO: Проверить, существует ли ученик в базе данных
    await state.update_data(selected_student=selected_student)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Установить расписание", "Назначить домашнее задание")
    await message.answer(reply_markup=keyboard)
    await TeacherState.choosing_action.set()


@learning_teacher_router.message(TeacherState.waiting_for_homework)
async def process_homework(message: types.Message, state: FSMContext):
    """Set new homework for student"""
    homework = message.text
    # TODO: Сохранить домашнее задание в базе данных
    await message.answer(f"Домашнее задание назначено: {homework}")
    await state.clear()


@learning_teacher_router.message(TeacherState.choosing_action)
async def choose_action(message: types.Message, state: FSMContext):
    action = message.text
    data = await state.get_data()
    selected_student = data.get("selected_student")

    if action == "Установить расписание":
        await message.answer(f"Введите расписание для {selected_student} в формате: День - Время")
        await TeacherState.waiting_for_schedule.set()
    elif action == "Назначить домашнее задание":
        await message.answer(f"Введите домашнее задание для {selected_student}.")
        await TeacherState.waiting_for_homework.set()
    else:
        await message.answer("Неверное действие. Попробуйте снова.")


@learning_teacher_router.message(TeacherState.waiting_for_schedule)
async def process_schedule(message: types.Message, state: FSMContext):
    schedule = message.text
    data = await state.get_data()
    selected_student = data.get("selected_student")
    # TODO: Сохранить расписание в базе данных
    await message.answer(f"Расписание для {selected_student} установлено: {schedule}")
    await state.clear()


@learning_teacher_router.message(TeacherState.waiting_for_homework)
async def process_homework(message: types.Message, state: FSMContext):
    homework = message.text
    data = await state.get_data()
    selected_student = data.get("selected_student")
    # TODO: Сохранить домашнее задание в базе данных
    await message.answer(f"Домашнее задание для {selected_student} назначено: {homework}")
    await state.clear()
