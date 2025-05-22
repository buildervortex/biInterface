from database.db import Database
from view.view import initUI

if __name__ == "__main__":
    db: Database = Database()

    if not db.connect():
        exit(1)

    initUI()
