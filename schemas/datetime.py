from typing import Optional, TypedDict
from dataclasses import dataclass, field
from enum import Enum


@dataclass(frozen=True, slots=True)
class TimeData:
    hour: int
    minute: int


class DateLesson(TypedDict):
    time: TimeData
    day: str


class DayWeek(str, Enum):
    monday: str = "mon"
    tuesday: str = "tue"
    wednesday: str = "wed"
    thuesday: str = "tue"
    friday: str = "fri"
    saturday: str = "sat"
    sunday: str = "sun" 
    