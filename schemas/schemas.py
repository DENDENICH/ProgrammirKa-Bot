from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True, slots=True)
class Student:
    name: str
    contact: str

