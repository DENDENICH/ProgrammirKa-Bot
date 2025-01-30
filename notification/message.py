import random
from config import bot

homework_dialog = [
    "Хэй, пора выполнить домашнее задание!",
    "Кажется, ты забыл про домашку... Надо это исправить!",
    "Домашка скучает по тебе :(" # TODO: смайлик
]


async def notification_homework_student(chat_id: int) -> str:
    message = random.choice(homework_dialog)
    await bot.send_message(chat_id, message)


async def notification_homework_teacher(
        name_student: str,
        chat_id: int
) -> str:
    await bot.send_message(
        chat_id, 
        f"У {name_student} был урок. Пора задать новую домашку"
        )
    
