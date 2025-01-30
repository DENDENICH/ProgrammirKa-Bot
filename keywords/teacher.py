from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# keyword for choose action on student
action_on_student = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Назначить новое домашнее задание",
            callback_data="set_homework"
        )],
        [InlineKeyboardButton(
            text="Установить расписание",
            callback_data="set_schedule"
        )]
    ]
)

exists_lesson = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Да",
            callback_data="yes_complete_lesson"
        )],
        [InlineKeyboardButton(
            text="Нет",
            callback_data="no_complete_lesson"
        )]
    ]
)
