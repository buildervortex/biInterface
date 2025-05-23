from database.db import Database


class FeatureRepository:

    def __init__(self, db: Database):
        self.db = db

    def registerDeliveringCustomer(self, firstName: str, lastName: str, nic: str, vehicleNumber: str, additionalDetails: str):
        query1: str = f"insert into known_customer(first_name,last_name,nic) values ('{firstName}','{lastName}','{nic}')"

        result = self.db.execinsert(query1)

        if result == None:
            return

        query2: str = f"select * from known_customer where nic = '{nic}'"

        data = self.db.exec(query2)

        if data == None:
            return

        rows = data.fetchall()

        print(rows[0])

        id = rows[0].id
        query4: str = f"insert into delivering_customer(vehicle_number,additional_details,known_customer_id) values ('{vehicleNumber}','{additionalDetails}',{id})"

        result = self.db.execinsert(query4)
        if result == None:
            print("error occoured")
