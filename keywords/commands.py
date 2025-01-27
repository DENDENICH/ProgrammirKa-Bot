from aiogram.types import BotCommand


teacher_command = [
    BotCommand(command="edit_student", description="Выбрать ученика"),
]

student_command = [
    BotCommand(command="get_help_homework", description="Помощь с домашкой"),
    BotCommand(command="homework", description="Домашнее задание"),
]
