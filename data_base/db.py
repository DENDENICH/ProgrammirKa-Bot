import sqlite3


class User:
    """Class for works with db sqlite3"""
    def __init__(self, path: str = "prog_db.db"):
        
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        self.cur.execute("""CREATE TABLE user IF NOT EXISTS (
                         id INTEGER PRIMARY KEY;
                         name TEXT;
                         contact TEXT;
                         homework TEXT;
                         progress_stage TEXT;
                         learning_programm INTEGER
                         )
                         """)

    def register_user() -> None:
        """Method for register user"""
        pass


    def set_homework() -> None:
        """Method for set new homework"""
        pass


    def set_progress_stage() -> None:
        """Method for set new progress_stage"""
        pass
    