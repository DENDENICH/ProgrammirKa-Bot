from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from schemas.datetime import DateLesson
from config import tg_config

from notification_functions import(
    check_and_notification_homework_student,
    check_conducted_lesson
)

from utils.parse_data import get_id_notification_homework


# initialize scheduler
scheduler = AsyncIOScheduler()


def notifications_homework_student(
    schedulers: list[DateLesson],
    student_id: int
) -> None:
    # Create notifications for homework. 
    # Excluding those days when a lesson is assigned
    for sch in schedulers:
        
        # Create unique id 
        id_notifi = get_id_notification_homework(
            tg_id=student_id,
            custom_prefix=f"{sch['time'].hour}:{sch['time'].minute}"
        )

        # Trigger day 
        time = CronTrigger(
            day_of_week=sch.get_string_lesson_days(),
            hour=sch['time'].hour + 1, # get notice after lesson
            minute=sch['time'].minute
        )

        # Create job 
        scheduler.add_job(
            func=check_and_notification_homework_student,
            kwargs={'student_id': student_id},
            trigger=time,
            id=id_notifi
        )


def create_notifications_homework_teacher(
        schedulers: list[DateLesson],
        student_id: int,
        teacher_id: int = tg_config.admin_id
) -> None:
    for sch in schedulers:
        scheduler.add_job(
            func=check_conducted_lesson,
            kwargs={'student_id': student_id, 'teacher_id': teacher_id},
            trigger=CronTrigger(
                day_of_week=sch.get_string_lesson_days(),
                hour=sch.hour + 1, # get notice after lesson
                minute=sch.minute,
            )
        )
