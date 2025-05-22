from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository


class UI:
    def __init__(self, repo: BiDashboardRepository):
        self.repository = repo
        print("ui initialized")

    def run(self):
        pass
