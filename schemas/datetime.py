from typing import Optional, TypedDict
from dataclasses import dataclass, field
from enum import Enum


class DateLesson(TypedDict):
    time: str
    day: str


class DayWeek(str, Enum):
    monday: str = "mon"
    tuesday: str = "tue"
    wednesday: str = "wed"
    thuesday: str = "tue"
    friday: str = "fri"
    saturday: str = "sat"
    sunday: str = "sun" 
    