from aiogram.types import BotCommand


teacher_command = [
    BotCommand(command="edit_student", description="Выбрать ученика"),
]

student_command = [
    BotCommand(command="get_help_homework", description="Чат с AI помощником"),
    BotCommand(command="homework", description="Домашнее задание"),
    BotCommand(command="help", description="Помощь в навигации"),
]
