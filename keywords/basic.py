from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# key for cancel action
cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Назад",
            callback_data="cancel"
        )]
    ]
)