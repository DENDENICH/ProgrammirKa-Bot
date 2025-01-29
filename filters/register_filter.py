from aiogram.types import Message
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


def check_user_exists(message: Message) -> bool:
    """Check exists student in data base"""
    return True if data_base.get_user(tg_id=message.id) else False
