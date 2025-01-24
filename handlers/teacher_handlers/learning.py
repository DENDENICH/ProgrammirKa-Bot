from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import parse_datetime


learning_teacher_router = Router()


class State(StatesGroup):
    """State for choose student"""
    choosing_student = State()
    choosing_action = State()
    fill_homework = State()
    fill_schedule = State()



# command /manage_student
# choose student
@learning_teacher_router.message(Command("manage_student"))
async def manage_students(message: Message, state: FSMContext):
    """Handler for choose student"""
    students = None # получение учеников из базы данных
    # выгрузка всех учеников из базы данных
    # загрузка в машину состояний для дальнейшего общения между хендлерами
    # Вывод списка учеников и кнопок с именем ученика
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*students)
    await message.answer("Выберите ученика:", reply_markup=keyboard)
    await state.set_state(State.choosing_student) # set state after choosing student


# Handler will be trigered if choosing student
@learning_teacher_router.message(StateFilter(State.choosing_student))
async def choose_student(message: Message, state: FSMContext):
    """Reading choose student for edit his data"""
    selected_student = message.text.strip()
    # TODO: Проверить, существует ли ученик в базе данных
    # await state.update_data(selected_student=selected_student)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # TODO: Сделать клавиатуру для выбора действий
    keyboard.add(
        "Установить расписание", 
        "Назначить домашнее задание"
        )
    await message.answer(reply_markup=keyboard)
    await state.set_state(State.choosing_action.set())



# command /set_schedule:
# Handler for set state for schedule
@learning_teacher_router.message(
    StateFilter(State.choosing_action),
    Command(commands="set_schedule")
    )
async def choose_schedule(message: Message, state: FSMContext):
    """Set state schedule for set schedule"""
    # data = await state.get_data()
    # selected_student = data.get("selected_student")
    # TODO: получение расписания из БД или машины состояний
    exists = None
    await message.answer(
        "Текущее расписание \n"
        f"{exists}\n"
        "Новое расписание:\n"
        "Формат:\n"
        "<день недели> - <время>\n<день недели> - <время>"
    )
    await state.set_data(State.fill_schedule)


# command /set_homework:
# Handler for set state for homework
@learning_teacher_router.message(
    StateFilter(State.choosing_action),
    Command(commands="set_homework")
    )
async def choose_homework(message: Message, state: FSMContext):
    """Set state homework for set homework"""
    # data = await state.get_data()
    # selected_student = data.get("selected_student")
    # TODO: получение домашнего задания из БД или машины состояний
    exists = None
    await message.answer(
        "Текущее задание:\n"
        f"{exists}\n"
        "Новое домашнее задание:"
    )
    await state.set_data(State.fill_homework)



# This handler will trigered if homework state is active
@learning_teacher_router.message(StateFilter(State.fill_homework))
async def process_homework(message: Message, state: FSMContext):
    """Set new homework for student"""
    homework = message.text
    # TODO: Сохранить домашнее задание в базе данных
    await message.answer(f"Домашнее задание назначено")
    await state.clear()


# This handler will trigered if schedule state is active
@learning_teacher_router.message(StateFilter(State.fill_schedule))
async def process_schedule(message: Message, state: FSMContext):
    """Set new shedule for student, parsing time"""
    schedules_time = parse_datetime.parse_schedule(schedule=message.text)
    # data = await state.get_data()
    # selected_student = data.get("selected_student")
    # TODO: Сохранить расписание в базе данных
    await message.answer(f"Расписание установлено")
    await state.clear()

