import random

homework_dialog = [
    "Хэй, пора выполнить домашнее задание!",
    "Кажется, ты забыл про домашку... Надо это исправить!",
    "Домашка скучает по тебе :(" # TODO: смайлик
]


def notification_homework_student() -> str:
    return random.choice(homework_dialog)


def notification_homework_teacher(
        name_student: str,
) -> str:
    return f"У {name_student} был урок. Пора задать новую домашку"
    

