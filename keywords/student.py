from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# keyword for choose complete_homework on student
complete_homework = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Я сделал домашнее задание!",
            callback_data="complete_homework"
        )]
    ]
)


# keyword for choose complete_homework on student
go_to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Завершить чат",
            callback_data="go_to_menu"
        )]
    ]
)
