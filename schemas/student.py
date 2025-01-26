
from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True, slots=True)
class StudentRegistry:
    name: str
    contact: str


@dataclass(frozen=True, slots=True)
class StudentModel:
    id: int
    tg_id: int
    name: str
    contact: str
    homework: str
    homework_completed: bool
    count_help_homework: int

