
from dataclasses import dataclass



@dataclass(frozen=True, slots=True)
class Student:
    name: str
    contact: str
    tg_id: int


# @dataclass(frozen=True, slots=True)
# class StudentModelDB:
#     id: int
#     tg_id: int
#     name: str
#     contact: str
#     homework: str
#     homework_completed: bool
#     count_help_homework: int

