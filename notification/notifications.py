from typing import Callable
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from schemas.datetime import DateSchedule


# initialize scheduler
scheduler = AsyncIOScheduler()


async def save_notification_homework_student(
    schedulers: list[DateSchedule],
    user_id: int
) -> None:
    # создание уведомлений по домашней работе
    # исключение тех дней, когда назначен урок
    pass