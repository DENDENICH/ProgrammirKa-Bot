from aiogram import (
    Router,
    F
)
from aiogram.filters import (
    CommandStart,
    StateFilter
)
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config import tg_config
from utils.register_key import keys
from filters import filters

from schemas.student import StudentRegistryBot


register_student_router = Router()


# Состояния для регистрации учеников
class RegistrationFSM(StatesGroup):
    """Registration state for input register data"""
    fill_key = State()
    fill_name = State()
    fill_contact = State()
    fill_schedule = State()


# command /register
# putting the bot in a key input waiting state
@register_student_router.message(
    CommandStart(),
    lambda message: message.id not in tg_config.admin_id,
    filters.check_user_exists  # check key exists in storage before registration
    )
async def start(message: Message, state: FSMContext):
    """Getting key for registration"""
    await message.answer(
        "Привет!\n"
        "Перед началом работы давай зарегестрируемся в боте\n"
        "Введи свой регистрационный ключ для начала:"
    )
    await state.set_state(RegistrationFSM.fill_key)


# This handler will be triggered if key is entered
@register_student_router.message(StateFilter(RegistrationFSM.fill_key))
async def process_registration_key(message: Message, state: FSMContext):
    """Process checking key and state for set name"""
    registration_key = message.text.strip()
    if registration_key in keys.get_all_keys(): # get all keys from file
        await message.answer(
            "Ключ подтвержден!"
            "Теперь введи свое имя (имя ученика)"
        )
        keys.delete_key(key=registration_key) # delete exists key from file
        await state.set_state(RegistrationFSM.fill_name) # set name state
    else:
        await message.answer(
            "Хм...\n"
            "Ключ не верный!"
        )


# This handler will be triggered if name is correct
@register_student_router.message(StateFilter(RegistrationFSM.fill_name), F.text.strip().isalpha())
async def process_phone_number(message: Message, state: FSMContext):
    """Read name and process phone number"""
    await state.update_data(name=message.text.strip())
    await message.answer(f"Теперь введи номер телефона ученика")
    await state.set_state(RegistrationFSM.fill_contact)


# This handler will be triggered if name is incorrect
@register_student_router.message(StateFilter(RegistrationFSM.fill_name))
async def name_incorrect(message: Message, state: FSMContext):
    """If name incorrect"""
    # save name in storage by key "name"
    await message.answer(
        "Кажется, это не похоже на имя..."
        "Пожалуйста, введите ваше имя, или имя ученика, если вы таковым не являетесь"
    )



# This handler will be triggered if contact is correct
@register_student_router.message(
    StateFilter(RegistrationFSM.fill_contact),
    filters.is_correct_phone_number
)
async def process_schedules(message: Message, state: FSMContext):
    """Read phone number and process input schedules"""
    # save contact in storage by key "contact"
    await state.update_data(phone_number=message.text.strip())
    await message.answer(
        "Хорошо, а теперь время установить расписание!\n\n"
        "*Формат ввода расписания:*\n"
        "<день недели> - <время (16:00)>\n<день недели> - <время (16:00)>\n\n"
        "*Или:*\n"
        "<день недели> - <время (16:00)>; <день недели> - <время (16:00)>"
    )
    await state.set_state(RegistrationFSM.fill_schedule)


# This handler will be triggered if contact is incorrect
@register_student_router.message(StateFilter(RegistrationFSM.fill_contact),)
async def incorrect_phone_number(message: Message, state: FSMContext):
    """If phone number is incorrect"""
    await message.answer(
        "Это не похоже на номер телефона или же он не является российским"
        "Пожалуйста, введите номер телефона ученика"
    )



# This handler will be triggered if user is registry
# This registration his schedule
@register_student_router.message(StateFilter(RegistrationFSM.fill_schedule))
async def register_user(message: Message, state: FSMContext):
    """Read shedulers and process register user"""
    # TODO: сохранение данных пользователя в датакласс, затем в базу данных
    data_user = await state.get_data
    await state.clear() # clear state
