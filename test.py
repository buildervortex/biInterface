from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository
from repository.featureRepository import FeatureRepository

db: Database = Database()
db.connect()

repository = BiDashboardRepository(db=db)
functionRepo = FeatureRepository(db)

print(repository.getLoanFinishedUnfinishedCount("2024-04-05"))

print(repository.getGasIncomes())
# print(repository.getLoanFinishedUnfinishedCount("2024-04-05"))
# print(repository.getGasIncome())

# print(repository.getEmptySellingIncomeProfit())

# print(repository.getEachManagerTransactionCount())

print(repository.getVehicleTransactionCounts())

print(repository.getUnFinishedLoanBalanceCountAll())

print(repository.getRegAndUnregCustomerCounts())

print(repository.getCylinderCountFromUserToGiveUs())

print(repository.getSystemUsersHandledTransactionCount())

print(repository.getCylinderTypeBySellCount())
# print(repository.getSellingIncomeProfit())

# functionRepo.registerDeliveringCustomer(
#     "lahiru", "dilhara", "199034567496V", "447859", None)

print(repository.getActiveLoanAcount())