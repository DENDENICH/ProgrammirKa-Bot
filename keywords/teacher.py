from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from schemas.student import Student


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


def get_keywords_of_students(students: list[Student]) -> InlineKeyboardMarkup:
    """get keywords of students

    Args:
        students (list[Student]): models students from db

    Returns:
        InlineKeyboardMarkup: inline keywords
    """
    keyboard = [[InlineKeyboardButton(
        text=student.name,
        callback_data=f"edit-{student.tg_id}-{student.name}"
    )] for student in students]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_keywords_of_complete_homework(tg_id: int):
    """get keywords of complete homework

    Args:
        tg_id (int): id students for add his in command
    """

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Да",
                callback_data=f"yes_complete_lesson-{tg_id}"
            )],
            [InlineKeyboardButton(
                text="Нет",
                callback_data=f"no_complete_lesson-{tg_id}"
            )]
        ]
    )
