from aiogram import Router, F
from aiogram.filters import (
    Command,
    StateFilter
)
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keywords.student import go_to_menu
from data_base import data_base

from schemas.homework import HomeworkInformation


help_homework_student_router = Router()



class AIHelpChatFSM(StatesGroup):
    chat = State()
    homework_inf: HomeworkInformation


# command /get_help_homework
# install state for chat with ai helper, export homework in fsm
@help_homework_student_router.message(Command("get_help_homework"))
async def help_homework(message: Message, state: FSMContext):
    # TODO: api с языковой моделью для помощи по домашней работе
    homework_inf = await data_base.get_homework(tg_id=message.id)
    if homework_inf.count_help_homework > 0:
        await message.answer(
            "Чат с AI помощником начался! Задавай свой вопрос"
            f"*Подсказок осталось:* **{homework_inf.count_help_homework}**",
             reply_markup=go_to_menu
        )
        await state.set_data(homework_inf=homework_inf)
        await state.set_state(AIHelpChatFSM.chat)
    else:
        await message.answer(
            "Для этого задания у тебя кончились подсказки"
            "Не отчаивайся! Сконцетрируйся на задании и все получится"
            )



# for dialog with chat_ai
@help_homework_student_router.message(StateFilter(AIHelpChatFSM.chat))
async def chat(message: Message, state: FSMContext):
    # TODO: api с языковой моделью для помощи по домашней работе
    homework_inf: HomeworkInformation = await state.get_data('homework_inf')
    if homework_inf.count_help_homework > 0:
        # TODO: метод для отправки и получения ответа от ai модели
        answer_ai = None
        await message.answer(
            f"{answer_ai}"
            f"*Подсказок осталось:* **{homework_inf.count_help_homework}**",
            reply_markup=go_to_menu
        )
        homework_inf.count_help_homework -= 1
        state.set_data(homework_inf=homework_inf)
    else:
        await message.answer(
            "Для этого задания у тебя кончились подсказки :("
            "Не отчаивайся! Сконцетрируйся на задании и все получится :)"
            )


# TODO: хендлер для отмены состояния и фиксации оставшихся попыток
@help_homework_student_router.message(
    StateFilter(AIHelpChatFSM.chat),
    F.data == "go_to_menu"
    )
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    homework_inf: HomeworkInformation = await state.get_data('homework_inf')
    data_base.set_new_count_help_homework(
        tg_id=callback.chat.id,
        new_count_help_homework=homework_inf.count_help_homework
    )
    await state.clear()
    await callback.answer(
        "Чат завершен"
        )
