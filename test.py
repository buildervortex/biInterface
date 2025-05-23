from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository

db: Database = Database()
db.connect()

repository = BiDashboardRepository(db=db)

print(repository.getLoanFinishedUnfinishedCount("2024-04-05"))

print(repository.getEmptySellingIncomeProfit())

print(repository.getEachManagerTransactionCount())

