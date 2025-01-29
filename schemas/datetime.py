from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True, slots=True)
class DateSchedule:
    hour: int
    minute: int
    day_week: str


class DayWeek(str, Enum):
    monday: str = "mon"
    tuesday: str = "tue"
    wednesday: str = "wed"
    thuesday: str = "tue"
    friday: str = "fri"
    saturday: str = "sat"
    sunday: str = "sun" 
    