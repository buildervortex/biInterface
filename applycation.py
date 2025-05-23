from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository
from repository.featureRepository import FeatureRepository

db: Database = Database()
db.connect()

functionRepo = FeatureRepository(db)

functionRepo.registerDeliveringCustomer(
    "lahiru", "dilhara", "199034567496V", "447859", None)