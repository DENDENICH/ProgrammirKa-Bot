from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup
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


# command /manage_student
# choose student
@learning_teacher_router.message(Command("manage_student"))
async def manage_students(message: Message):
    """Handler for choose student"""
    students = None # получение учеников из базы данных
    # выгрузка всех учеников из базы данных
    # загрузка в машину состояний для дальнейшего общения между хендлерами
    # Вывод списка учеников и кнопок с именем ученика
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*students)
    await message.answer("Выберите ученика:", reply_markup=keyboard)
    await TeacherState.choosing_student.set()


@learning_teacher_router.message(TeacherState.choosing_student)
async def choose_student(message: Message, state: FSMContext):
    """Reading choose student for edit his data"""
    selected_student = message.text.strip()
    # TODO: Проверить, существует ли ученик в базе данных
    await state.update_data(selected_student=selected_student)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Установить расписание", "Назначить домашнее задание")
    await message.answer(reply_markup=keyboard)
    await TeacherState.choosing_action.set()


@learning_teacher_router.message(TeacherState.waiting_for_homework)
async def process_homework(message: Message, state: FSMContext):
    """Set new homework for student"""
    homework = message.text
    # TODO: Сохранить домашнее задание в базе данных
    await message.answer(f"Домашнее задание назначено: {homework}")
    await state.clear()


@learning_teacher_router.message(TeacherState.choosing_action)
async def choose_action(message: Message, state: FSMContext):
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
async def process_schedule(message: Message, state: FSMContext):
    schedule = message.text
    data = await state.get_data()
    selected_student = data.get("selected_student")
    # TODO: Сохранить расписание в базе данных
    await message.answer(f"Расписание для {selected_student} установлено: {schedule}")
    await state.clear()


@learning_teacher_router.message(TeacherState.waiting_for_homework)
async def process_homework(message: Message, state: FSMContext):
    homework = message.text
    data = await state.get_data()
    selected_student = data.get("selected_student")
    # TODO: Сохранить домашнее задание в базе данных
    await message.answer(f"Домашнее задание для {selected_student} назначено: {homework}")
    await state.clear()
