from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# keyword for choose action on student
action_on_student = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Назначить новое домашнее задание",
            callback_data="set_homework"
        )],
        [InlineKeyboardButton(
            text="Назначить новое расписание",
            callback_data="set_schedule"
        )]
    ]
)

cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Назад",
            callback_data="cancel"
        )]
    ]
)