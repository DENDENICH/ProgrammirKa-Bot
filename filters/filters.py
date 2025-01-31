from aiogram.types import Message, CallbackQuery
import re

from data_base import data_base


def is_correct_phone_number(message: Message) -> bool:
    """Check russian number phone.

        - startwith +7 or 8.
        - ten numbers.
        - space, defice is correct.
        """
    pattern = re.compile(r'^(\+7|8)\s*\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$')
    return bool(pattern.match(message.text.strip()))


async def check_user_exists(message: Message) -> bool:
    """Check exists student in data base"""
    return True if await data_base.get_user(tg_id=message.id) else False


def command_choose_student(callback: CallbackQuery) -> bool:
    """Filter for find choose student command"""
    return True if re.match(
        pattern=r"edit-[1-9]+-[A-Za-zА-Яа-я ]+",
        string=callback.data.strip()
    ) else False


def command_yes_complete_homework(callback: CallbackQuery) -> bool:
    """Filter for find yes complete homework command"""
    return True if re.match(
        pattern=r"yes_complete_lesson-[1-9]+",
        string=callback.data.strip()
    ) else False


def command_no_complete_homework(callback: CallbackQuery) -> bool:
    """Filter for find no complete homework command"""
    return True if re.match(
        pattern=r"no_complete_lesson-[1-9]+",
        string=callback.data.strip()
    ) else False
