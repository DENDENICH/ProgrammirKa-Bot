from aiogram.types import Message

import re

def is_correct_phone_number(message: Message) -> bool:
    """Проверяет, является ли строка корректным российским номером телефона.

        Правила:
        - startwith +7 or 8.
        - ten numbers.
        - space, defice is correct.
        """
    pattern = re.compile(r'^(\+7|8)\s*\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$')
    return bool(pattern.match(message.text.strip()))


def check_user_exists(message: Message) -> bool:
    # TODO: проверка присутствия ученика в БД по id его ТГ
    pass
