from typing import Callable
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from schemas.datetime import DateSchedule
from message import notification_homework_student, notification_homework_teacher
from config import tg_config

# initialize scheduler
scheduler = AsyncIOScheduler()


def create_notifications_homework_student(
    schedulers: list[DateSchedule],
    user_id: int
) -> None:
    # создание уведомлений по домашней работе
    # исключение тех дней, когда назначен урок
    for sched in schedulers:
        scheduler.add_job(
            func=notification_homework_student,
            args=[user_id],
            trigger=CronTrigger(
                day_of_week=sched.get_notice_days(),
                hour=sched.hour,
                minute=sched.minute,
            )
        )


def create_notifications_homework_student(
        schedulers: list[DateSchedule],
        user_id: int = tg_config.admin_id
) -> None:
    for sched in schedulers:
        scheduler.add_job(
            func=notification_homework_student,
            args=[user_id],
            trigger=CronTrigger(
                day_of_week=sched.get_lesson_days(),
                hour=sched.hour + 1, # get notice after lesson
                minute=sched.minute,
            )
        )
        


def delete_notification_homework_student():
    pass


def delete_notification_homework_teacher():
    pass
