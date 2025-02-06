from typing import Optional, TypedDict
from dataclasses import dataclass, field
from enum import Enum


class DateLesson(TypedDict):
    time: str
    day: str


# @dataclass(slots=True)
# class DateSchedule:
#     hour: int
#     minute: int
#     lesson_days_week: list[str]
#     not_lesson_days_week: Optional[list[str] | None] = field(default=None)

#     def __post_init__(self):
#         if not self.not_lesson_days_week:
#             self.not_lesson_days_week = self.get_list_not_lesson_days_week()

#     def get_list_not_lesson_days_week(self) -> list[str]:
#         pass

#     def get_string_not_lesson_days(self) -> str:
#         pass

#     def get_string_lesson_days(self) -> str:
#         pass


class DayWeek(str, Enum):
    monday: str = "mon"
    tuesday: str = "tue"
    wednesday: str = "wed"
    thuesday: str = "tue"
    friday: str = "fri"
    saturday: str = "sat"
    sunday: str = "sun" 
    