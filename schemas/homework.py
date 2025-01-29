from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HomeworkInformation:
    homework: str
    complete_homework: bool
    count_help_homework: int
