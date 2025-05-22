from dotenv import load_dotenv
import os
import pyodbc


class Database:

    def __init__(self):
        load_dotenv()
        self.conn: pyodbc.Connection = None
        self.cursor: pyodbc.Cursor = None

        self.server: str = os.getenv("DB_SERVER")
        self.database: str = os.getenv("DB_NAME")
        self.username: str = os.getenv("DB_USER")
        self.password: str = os.getenv("DB_PASSWORD")
        self.port: str = os.getenv("DB_PORT")

        self.connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL SERVER}};"
            f"SERVER={self.server},{self.port};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password}"
        )

    def init(self):
        pass

    def connect(self) -> bool:
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print("database connected")
            return True
        except Exception as e:
            print(e)
            return False

    def exec(self, query: str) -> pyodbc.Cursor:
        cursor = self.conn.cursor()

        try:
            cursor.execute(query)
            return cursor
        except Exception as e:
            print(e)
            return None

    def disconnect(self):
        pass
