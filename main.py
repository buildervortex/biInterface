from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository
from view.view import UI

if __name__ == "__main__":
    db: Database = Database()

    if not db.connect():
        exit(1)

    repository = BiDashboardRepository(db=db)

    UI(repo=repository).run()
