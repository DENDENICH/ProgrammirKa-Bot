from typing import NamedTuple


class DataEditStudent(NamedTuple):
    name: str
    tg_id: int


def parse_data_edit_student(data: str) -> DataEditStudent:
    """Parse data student after edit"""
    _, tg_id, name = data.split('-')
    return DataEditStudent(name=name, tg_id=int(tg_id))


def parse_id_in_query_complete_homework(data: str) -> int:
    _, tg_id = data.split('-')
    return int(tg_id)


def get_id_notification_homework(
        tg_id: int,
        custom_prefix: str,
        main_prefix: str = "homework",
) -> str:
    pass


