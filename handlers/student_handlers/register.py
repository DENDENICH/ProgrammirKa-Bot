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

from utils import register_key
from filters import register_filter

from schemas import StudentModel

register_student_router = Router()


# Состояния для регистрации учеников
class RegistrationFSM(StatesGroup):
    """Registration state for input register data"""
    fill_key = State()
    fill_name = State()
    fill_contact = State()


# command /register
# putting the bot in a key input waiting state
@register_student_router.message(Command(commands='register'))
async def cmd_start(message: Message, state: FSMContext):
    """Getting key for registration"""
    await message.answer("Введите ваш регистрационный ключ для начала.")
    await state.set_state(RegistrationFSM.fill_key)


# This handler will be triggered if key is entered
@register_student_router.message(StateFilter(RegistrationFSM.fill_key))
async def process_registration_key(message: Message, state: FSMContext):
    """Process checking key"""
    registration_key = message.text.strip()
    valid_key = register_key.read_key().strip() # reading key from file

    if valid_key == registration_key:
        await message.answer(
            "Ключ подтвержден!"
            "Введите ваше имя, или имя ученика, если вы таковым не являетесь"
        )
        register_key.delete_key() # delete exists key from file
        await state.set_state(RegistrationFSM.fill_name) # set name state
    else:
        await message.answer("Неверный ключ. Попробуйте снова.")



# This handler will be triggered if name is correct
@register_student_router.message(StateFilter(RegistrationFSM.fill_name), F.text.strip().isalpha())
async def process_name(message: Message, state: FSMContext):
    """Process input name"""
    # save name in storage by key "name"
    await state.update_data(name=message.text.strip())
    await message.answer(f"Теперь введите номер телефона ученика")
    await state.set_state(RegistrationFSM.fill_contact)


# This handler will be triggered if name is incorrect
@register_student_router.message(StateFilter(RegistrationFSM.fill_name))
async def process_name(message: Message, state: FSMContext):
    """Process input name"""
    # save name in storage by key "name"
    await message.answer(
        "Кажется, это не похоже на имя..."
        "Пожалуйста, введите ваше имя, или имя ученика, если вы таковым не являетесь"
    )



# This handler will be triggered if contact is correct
@register_student_router.message(
    StateFilter(RegistrationFSM.fill_contact),
    register_filter.is_correct_phone_number
)
async def process_name(message: Message, state: FSMContext):
    """Process input name"""
    # save contact in storage by key "contact"
    await state.update_data(contact=message.text.strip())
    await message.answer(f"Отлично, вы зарегестрированы :)")

    # TODO: сохранение данных пользователя в датакласс, затем в базу данных
    await state.clear() # clear state


# This handler will be triggered if contact is incorrect
@register_student_router.message(StateFilter(RegistrationFSM.fill_contact),)
async def process_name(message: Message, state: FSMContext):
    """Process input name"""
    await message.answer(
        "Это не похоже на номер телефона или же он не является российским"
        "Пожалуйста, введите номер телефона ученика"
    )
