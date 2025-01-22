import sqlite3


class DB:
    """Class for works with db sqlite3"""
    def __init__(self, path: str = "prog_db.db"):
        
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def register_user(
            name: str,
            contact: str
    ) -> None:
        pass
    