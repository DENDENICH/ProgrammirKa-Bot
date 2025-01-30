from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HomeworkInformation:
    homework: str
    status_homework: bool
    count_help_homework: int
