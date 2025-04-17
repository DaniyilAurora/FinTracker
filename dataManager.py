import sqlite3


class DataManager():
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.cursor = self.connection.cursor()

        self.__initialiseDatabase()

    def __initialiseDatabase(self):
        if self.__isFirstLaunch():
            print("Creating tables...")
            # Create passwords table
            self.cursor.execute("""
                CREATE TABLE passwords(
                    accID INTEGER PRIMARY KEY,
                    username VARCHAR(255),
                    password VARCHAR(255)
                );
            """)

            self.connection.commit()

            # Create transactions table
            self.cursor.execute("""
                CREATE TABLE transactions(
                    accID INTEGER PRIMARY KEY,
                    origin TEXT,
                    amount REAL
                );
            """)

            self.connection.commit()
        else:
            print("Tables already exist")

    def __isFirstLaunch(self):
        # Check is table "passwords" exists
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, ("passwords",))

        result = self.cursor.fetchone()

        return result is None

    def getPassword(self, username: str):
        # Get password by username
        self.cursor.execute("""
            SELECT password FROM passwords
            WHERE username=?;
        """, (username,))

        result = self.cursor.fetchone()
        if result is None:
            return None
        
        return str(result[0])