from dataclasses import dataclass
from datetime import time

from schemas.datetime import DateLesson, DayWeek


def parse_schedule(schedule: str) -> list[DateLesson]:
    """Parse all date from string schedules
    
    :param schedule: строка с расписанием.
    :return: список объектов datetime.
    """
    
    # split all date
    lines = schedule.split("\n")
    result = []
    
    for line in lines:
        if not line.strip():
            continue
        day, t = line.split(" - ")
        day, t = int(day.strip()), t.strip()
        
        if day not in ['pass']:
            raise ValueError(f"Некорректный день недели: {day}")
        
        # parsing time
        hours, minutes = map(int, t.split(":"))
        result.append(
            DateSchedule(
        time_scheldue=time(hour=hours, minute=minutes),
        day_week=DayWeek[day]
        )
    )
        
    return result


print(DayWeek.find('week'))
