from typing import NamedTuple


class DataEditStudent(NamedTuple):
    name: str
    id: int


def parse_data_edit_student(data: str) -> DataEditStudent:
    """Parse data student after edit"""
    _, id, name = data.split('-')
    return DataEditStudent(name=name, id=int(id))


def parse_id_in_query_complete_homework(data: str) -> int:
    _, id = data.split('-')
    return int(id)
