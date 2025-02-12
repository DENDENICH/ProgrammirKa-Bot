from dataclasses import dataclass
from datetime import time

from schemas.datetime import DateLesson, DayWeek, TimeData


def parse_schedule(schedule: str) -> list[DateLesson]:
    """Parse all date from string schedules
    
    :param schedule: string for schedule.
    :return: list DateLesson.
    """
    
    # split all date
    lines = schedule.split("\n")
    result = []
    
    for line in lines:
        if not line.strip():
            continue
        day, t = line.split(" - ")
        day, t = int(day.strip()), t.strip()
        
        if day not in DayWeek:
            raise ValueError(f"Некорректный день недели: {day}")
        
        # parsing time
        hours, minutes = map(int, t.split(":"))
        result.append(
            DateLesson(
                day=day,
                time=TimeData(
                    hour=hours,
                    minute=minutes
                )
            )
    )
        
    return result
