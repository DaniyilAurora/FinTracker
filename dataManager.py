import sqlite3


class DataManager():
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.cursor = self.connection.cursor()

        #self.cursor.execute("INSERT INTO transactions VALUES (5, '1', 'Friend', 10.00)")
        #self.connection.commit()

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
                    transactionID INTEGER PRIMARY KEY,
                    username VARCHAR(255),
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

    def getTransactions(self, username: str):
        # Get transactions by username
        self.cursor.execute("""
            SELECT * FROM transactions
            WHERE username=?;
        """, (username,))
        result = self.cursor.fetchall()
        return result

    def addTransaction(self, username: str, type: str, amount: float):
        # Add new transaction to the database
        self.cursor.execute("""
            INSERT INTO transactions 
            (username, origin, amount) 
            VALUES (?, ?, ?);
        """, (username, type, amount))
        self.connection.commit()
        
        # Means everything was successful
        return True