from data_base import data_base
from message import (
    notification_homework_teacher,
    notification_homework_student
)
from schemas.homework import HomeworkInformation
from config import tg_config


async def _get_status_homework(student_id: int) -> HomeworkInformation:
    """Method for get status homework"""
    homework = await data_base.get_homework(tg_id=student_id)
    return homework.status_homework


async def check_and_notification_homework_student(student_id: int) -> None:
    """Method for check and notification homework for student"""
    status = await _get_status_homework(student_id=student_id)
    if not status and status is not None: # if not complete and status is not None
        await notification_homework_student(student_id=student_id)


async def check_conducted_lesson(
        student_id: int,
        teacher_id: int
) -> None:
    """Method for send notification about check conducted lesson for teacher"""
    student = await data_base.get_user(tg_id=student_id)
    await notification_homework_teacher(
        teacher_id=teacher_id,
        name_student=student.name
    )



