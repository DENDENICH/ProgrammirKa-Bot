import random
from config import bot, tg_config
from keywords.teacher import get_keywords_of_complete_homework

homework_dialog = [
    "Хэй, пора выполнить домашнее задание!",
    "Кажется, ты забыл про домашку... Надо это исправить!",
    "Домашка скучает по тебе 😢"
]


async def notification_homework_student(student_id: int) -> None:
    message = random.choice(homework_dialog)
    await bot.send_message(student_id, message)


async def notification_homework_teacher(
        name_student: str,
        student_id: int,
        teacher_id: int
) -> None:
    await bot.send_message(
        chat_id=teacher_id,
        text=f"Был ли проведен урок у **{name_student}**?",
        reply_markup=get_keywords_of_complete_homework(tg_id=student_id)
        )
