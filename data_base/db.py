import aiosqlite


class User:
    """Class for works with db sqlite3"""

    def __init__(self):
        self.connect = None


    async def initialize_bd(self, path: str = "db.db"):
        """Initialize bd, create tables
        :param path: path to file database
        """
        self.connect = await aiosqlite.connect(path)

        # initialize table user
        async with self.connect as connect:
            await connect.execute("""CREATE TABLE user IF NOT EXISTS (
                             id INTEGER PRIMARY KEY NOT NULL;
                             tg_id INTEGER UNIQUE NOT NULL
                             name TEXT NOT NULL;
                             contact TEXT NOT NULL;
                             homework TEXT;
                             homework_completed BOOLEAN NOT NULL;
                             count_help_homework INTEGER NOT NULL;
                             progress_stage TEXT NOT NULL;
                             )
                             """)

    async def register_user(self) -> None:
        """Method for register user"""
        pass


    async def set_homework(self) -> None:
        """Method for set new homework"""
        pass


    def set_progress_stage(self) -> None:
        """Method for set new progress_stage"""
        pass
    