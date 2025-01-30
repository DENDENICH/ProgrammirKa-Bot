from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from schemas.datetime import DateSchedule
from config import tg_config

from notification_functions import(
    check_and_notification_homework_student,
    check_conducted_lesson
)


# initialize scheduler
scheduler = AsyncIOScheduler()


def notifications_homework_student(
    schedulers: list[DateSchedule],
    student_id: int
) -> None:
    # создание уведомлений по домашней работе
    # исключение тех дней, когда назначен урок
    for sched in schedulers:
        scheduler.add_job(
            func=check_and_notification_homework_student,
            kwargs={'student_id': student_id},
            trigger=CronTrigger(
                day_of_week=sched.get_notice_days(),
                hour=sched.hour,
                minute=sched.minute,
            )
        )


def create_notifications_homework_teacher(
        schedulers: list[DateSchedule],
        student_id: int,
        teacher_id: int = tg_config.admin_id
) -> None:
    for sch in schedulers:
        scheduler.add_job(
            func=check_conducted_lesson,
            kwargs={'student_id': student_id, 'teacher_id': teacher_id},
            trigger=CronTrigger(
                day_of_week=sch.get_lesson_days(),
                hour=sch.hour + 1, # get notice after lesson
                minute=sch.minute,
            )
        )
