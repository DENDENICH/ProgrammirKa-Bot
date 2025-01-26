from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True, slots=True)
class DateSchedule:
    time_scheldue: time
    day_week: int



def parse_schedule(schedule: str) -> list[DateSchedule]:
    """Parse all date from string schedules
    
    :param schedule: строка с расписанием.
    :return: список объектов datetime.
    """
    # Словарь соответствий для дней недели
    days_of_week = {
        "Понедельник": 0,
        "Вторник": 1,
        "Среда": 2,
        "Четверг": 3,
        "Пятница": 4,
        "Суббота": 5,
        "Воскресенье": 6,
    }
    
    # split all date
    lines = schedule.split("\n")
    result = []
    
    for line in lines:
        if not line.strip():
            continue
        day, t = line.split(" - ")
        day, t = day.strip(), t.strip()
        
        if day not in days_of_week:
            raise ValueError(f"Некорректный день недели: {day}")
        
        # parsing time
        hours, minutes = map(int, t.split(":"))
        result.append(
            DateSchedule(
        time_scheldue=time(hour=hours, minute=minutes),
        day_week=days_of_week[day]
        )
    )
        
    return result
