from dataclasses import dataclass
from datetime import datetime, time


@dataclass(frozen=True, slots=True)
class DateScheldue:
    time_scheldue: time
    day_week: int



def parse_schedule(schedule: str) -> list[DateScheldue]:
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
            DateScheldue(
        time_scheldue=time(hour=hours, minute=minutes),
        day_week=days_of_week[day]
        )
    )
        
    return result

# # Пример использования
# schedule_str = """Понедельник - 14:30
# Среда - 09:00"""

# dates = parse_schedule(schedule_str)
# print(dates)
