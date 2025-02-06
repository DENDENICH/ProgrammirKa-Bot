import json
import aiosqlite

from schemas.datetime import DateLesson
from schemas.student import Student
from schemas.homework import HomeworkInformation


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
                             homework_completed BOOLEAN;
                             count_help_homework INTEGER;
                                )
                             """)


    async def get_users(self) -> list[Student]:
        """Method to get all users"""
        # TODO: переделать создание объекта StudentModel и столбцы данных извлечения
        users = list()
        async with self.connect as cursor:
            result = await cursor.execute("SELECT (tg_id, name, contact) FROM student")
            rows = await result.fetchall()
            for row in rows:
                users.append(Student(*row))
        return users


    async def get_user(self, tg_id: int) -> Student:
        """Method for get one user for checking exists"""
        async with self.connect as cursor:
            result = await cursor.execute("""SELECT (tg_id, name, contact) FROM student 
                                            WHERE tg_id = %s""",
                                            (tg_id,))
            user = await result.fetchone()
        return Student(*user)


    async def register_user(self, user: Student) -> None:
        """Method for register user"""
        async with self.connect as cursor:
            await cursor.execute("""INSERT INTO student 
                                (tg_id, name, contact)
                                VALUES (%s, %s, %s)""",
                                 (user.tg_id, user.name, user.contact,)
                                  )


    async def set_homework(
        self, 
        tg_id: int,
        new_homework: str
    ) -> None:
        """Method for set new homework"""
        async with self.connect as cursor:
            await cursor.execute("""INSERT INTO student 
                                (homework, homework_completed, count_help_homework)
                                VALUES (%s, %s, %s)
                                WHERE tg_id = %s""",
                                 (new_homework, True, 3, tg_id,)
                                )


    async def get_homework(self, tg_id: int) -> HomeworkInformation:
        """Method for get homework"""
        async with self.connect as cursor:
            result = await cursor.execute("""SELECT (homework, homework_completed, count_help_homework) FROM student 
                                          WHERE tg_id = %s""", 
                                          (tg_id,))
            homework = await result.fetchone()
        return HomeworkInformation(*homework)


    async def complete_homework(self, tg_id: int) -> None:
        """Method for complete homework"""
        async with self.connect as cursor:
            await cursor.execute("""INSERT INTO student 
                                homework_completed
                                VALUES (%s)
                                WHERE tg_id = %s""",
                                 (True, tg_id,)
                                )
    

    async def set_new_count_help_homework(
            self, 
            tg_id: int, 
            new_count_help_homework: int
        ) -> None:
        """division count help homework"""
        async with self.connect as cursor:
            await cursor.execute("""INSERT INTO student 
                                count_help_homework
                                VALUES (%s)
                                WHERE tg_id = %s""",
                                 (new_count_help_homework, tg_id,)
                                )



class JsonSchedule:
    """Class for works with json schedule"""

    def __init__(self, path: str = 'schedule.json'):
        self.path = path
        with open(self.path, encoding='utf-8') as file:
            self.data_schedule = json.load(file.read()) # load json from file


    def set_new_schedule(self, data: list[DateLesson], user_id: int):
        """Method for set new schedule and delete old on user"""
        self.data_schedule[str(user_id)] = data
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.data_schedule, file, ensure_ascii=False, indent=4) # save json to file


    def get_schedule(self, tg_id: int):
        """Method for get schedule on user"""
        pass

 
data_base = DataBase() # TODO: инициализировать базу данных
json_schedule = JsonSchedule()
