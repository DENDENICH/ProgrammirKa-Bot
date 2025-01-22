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
                        
                         )
                         """)

    def register_user(
            name: str,
            contact: str
    ) -> None:
        pass
    