from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True, slots=True)
class DateSchedule:
    hour: int
    minute: int
    day_week: list[str]


    def get_notice_days() -> str:
        pass


    def get_lesson_days() -> str:
        pass


class DayWeek(str, Enum):
    monday: str = "mon"
    tuesday: str = "tue"
    wednesday: str = "wed"
    thuesday: str = "tue"
    friday: str = "fri"
    saturday: str = "sat"
    sunday: str = "sun" 
    