from database.db import Database


class BiDashboardRepository:

    def __init__(self, db: Database):
        self.db = db
