from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Student:
    name: str
    contact: str
    tg_id: int


class StudentKeyDataFSM(str, Enum):
    """Class for using key in fsm machines"""
    name = "name"
    tg_id = "tg_id"
    contact = "contact"


# @dataclass(frozen=True, slots=True)
# class StudentModelDB:
#     id: int
#     tg_id: int
#     name: str
#     contact: str
#     homework: str
#     homework_completed: bool
#     count_help_homework: int

