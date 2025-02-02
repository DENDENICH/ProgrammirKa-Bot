from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from utils import parse_datetime, parse_data

from data_base import data_base, json_schedule

from keywords.teacher import action_on_student, get_keywords_of_students
from keywords.basic import cancel

from filters.filters import(
    command_choose_student,
    command_yes_complete_homework,
    command_no_complete_homework
)

from schemas.student import StudentKeyDataFSM


learning_teacher_router = Router()


class FSMLearning(StatesGroup):
    """State for choose student"""
    choose_student = State()
    choosing_action = State()
    fill_homework = State()
    fill_schedule = State()
    set_new_homework = State() 



# command /manage_student
# choose student
@learning_teacher_router.message(Command("edit_student"))
async def manage_students(message: Message):
    """Handler for choose student"""
    students = await data_base.get_users()
    await message.answer(
        text="Выберите ученика:",
        reply_markup=get_keywords_of_students(students=students)
        )


# Handler will be trigered if choosing student
@learning_teacher_router.message(
        StateFilter(FSMLearning.choose_student),
        command_choose_student
        )
async def choose_student(callback: CallbackQuery, state: FSMContext):
    """Reading choose student for edit his data"""
    name, tg_id = parse_data.parse_data_edit_student(data=callback.data)
    await state.update_data({
        StudentKeyDataFSM.name: name,
        StudentKeyDataFSM.tg_id: tg_id
        })
    await callback.answer(
        text=f"Ученик {name}",
        reply_markup=action_on_student,
    )
    await state.set_state(FSMLearning.choosing_action)



# command /set_schedule:
# Handler for set state for schedule
@learning_teacher_router.message(
    StateFilter(FSMLearning.choosing_action),
    F.data == "set_schedule"
    )
async def choose_schedule(callback: CallbackQuery, state: FSMContext):
    """Set state schedule for set schedule"""
    tg_id = await state.get_value(StudentKeyDataFSM.tg_id)
    # TODO: получение расписания из БД или машины состояний
    exists_schedulers = json_schedule.get_schedule(tg_id=tg_id)
    await callback.message.edit_text(
        text="Текущее расписание \n"
        f"{exists_schedulers}\n"
        "Новое расписание:\n"
        "Формат:\n"
        "<день недели> - <время>\n<день недели> - <время>",
        reply_markup=cancel
    )
    await state.set_state(FSMLearning.fill_schedule)


# command /set_homework:
# Handler for set state for homework
@learning_teacher_router.message(
    StateFilter(FSMLearning.choosing_action),
    F.data == "set_homework"
    )
async def choose_homework(callback: CallbackQuery, state: FSMContext):
    """Set state homework for set homework"""
    # TODO: получение домашнего задания из БД или машины состояний
    tg_id = await state.get_value(StudentKeyDataFSM.tg_id)
    exists_homework = await data_base.get_homework(tg_id=tg_id)
    await callback.message.edit_text(
        text="Текущее задание:\n"
        f"{exists_homework.homework}\n"
        "Статус выполнения\n"
        f"{'Выполнен' if exists_homework.status_homework else 'Невыполнен'}"
        "Новое домашнее задание:",
        reply_markup=cancel
    )
    await state.set_state(FSMLearning.fill_homework)



# This handler will trigered if homework state is active
@learning_teacher_router.message(StateFilter(FSMLearning.fill_homework))
async def process_homework(message: Message, state: FSMContext):
    """Set new homework for student"""
    homework = message.text
    tg_id = await state.get_value(StudentKeyDataFSM.tg_id)
    try:
        await data_base.set_homework(
            tg_id=tg_id,
            homework=homework
        )
    except: # TODO: возвести в конструкцию try/except потенциально опасные места. Сделать кастомные обработчики ошибок
        await message.answer(f"Ошибка при сохранении домашнего задания")
    else:
        await message.answer(f"Домашнее задание назначено")
        await state.clear()


# This handler will trigered if schedule state is active
@learning_teacher_router.message(StateFilter(FSMLearning.fill_schedule))
async def process_schedule(message: Message, state: FSMContext):
    """Set new shedule for student, parsing time"""
    schedules_time = parse_datetime.parse_schedule(schedule=message.text)
    # data = await state.get_data()
    # selected_student = data.get("selected_student")
    # TODO: Сохранить расписание в базе данных
    await message.answer(f"Расписание установлено")
    await state.clear()



# This handler will trigered if lesson is not complete
@learning_teacher_router.message(command_no_complete_homework)
async def yes_complete_lesson(callback: CallbackQuery):
    """Notificate about new homework, stay relevant old homework"""
    await callback.message.edit_text(
        "Старое домашнее задание осталось актуальным"
    )


# This handler will trigered if lesson is yes complete
@learning_teacher_router.message(command_yes_complete_homework)
async def yes_complete_lesson(callback: CallbackQuery, state: FSMContext):
    """Notificate about new homework, and update nofications homework"""
    await state.set_data(
        {StudentKeyDataFSM.tg_id: parse_data.parse_id_in_query_complete_homework(data=callback.data)}
        )
    await callback.message.edit_text(
        "Назначьте новое домашнее задание:"
    )
    await state.set_state(FSMLearning.set_new_homework)


# This handler will trigered after input new homework
@learning_teacher_router.message(StateFilter(FSMLearning.set_new_homework))
async def yes_complete_lesson(message: Message, state: FSMContext):
    """Notificate about new homework, and update nofications homework"""
    tg_id = await state.get_value(StudentKeyDataFSM.tg_id)
    await data_base.set_homework(
        tg_id=tg_id,
        new_homework=message.text.strip()
        )
    await message.answer(
        "Новое домашнее задание назначено!"
    )
    await state.clear()
