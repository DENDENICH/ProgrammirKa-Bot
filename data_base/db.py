import json
import aiosqlite

from utils.parse_datetime import DateSchedule
from schemas.student import StudentModelDB, StudentRegistryBot


class DataBase:
    """Class for works with db sqlite"""

    def __init__(self):
        self.connect = None


    async def initialize_bd(self, path: str = "db.db"):
        """Initialize bd, create tables
        :param path: path to file database
        """
        self.connect = await aiosqlite.connect(path)

        # initialize table user
        async with self.connect as connect:
            await connect.execute("""CREATE TABLE student IF NOT EXISTS (
                             id INTEGER PRIMARY KEY NOT NULL;
                             tg_id INTEGER UNIQUE NOT NULL
                             name TEXT NOT NULL;
                             contact TEXT NOT NULL;
                             homework TEXT;
                             homework_completed BOOLEAN NOT NULL;
                             count_help_homework INTEGER NOT NULL;
                                )
                             """)


    async def get_users(self) -> list[StudentModelDB]:
        """Method to get all users"""
        users = list()
        async with self.connect as cursor:
            result = await cursor.execute("SELECT * FROM user")
            rows = await result.fetchall()
            for row in rows:
                users.append(StudentModelDB(*row))
        return users

    async def get_user(self, tg_id: int) -> tuple | None:
        """Method for get one user for checking exists"""
        async with self.connect as cursor:
            result = await cursor.execute("SELECT * FROM user WHERE tg_id = %d" % tg_id)
        return result

    async def register_user(self) -> None:
        """Method for register user"""
        pass


    async def set_homework(self) -> None:
        """Method for set new homework"""
        pass


    async def get_homework(self) -> None:
        """Method for get homework"""
        pass


    async def complete_homework(self) -> None:
        """Method for complete homework"""
        pass


    async def division_count_help_homework(self) -> None:
        """division count help homework"""
        pass



class JsonSchedule:
    """Class for works with json schedule"""

    def __init__(self, path: str = 'schedule.json'):
        self.path = path
        with open(self.path, encoding='utf-8') as file:
            self.data_schedule = json.load(file) # load json from file


    async def set_new_schedule(self, data: DateSchedule, user_id: int):
        """Method for set new schedule and delete old on user"""
        self.data_schedule[user_id] = json.dumps(data)
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.data_schedule, file, ensure_ascii=False) # save json to file


    async def get_schedule(self, tg_id: int):
        """Method for get schedule on user"""
        pass


data_base = DataBase()
json_schedule = JsonSchedule()
