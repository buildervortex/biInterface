from database.db import Database


class BiDashboardRepository:

    def __init__(self, db: Database):
        self.db = db

    def getStock(self, inventory_id: int) -> list[tuple[str, int, int]]:
        query: str = f"select ct.display_name,cs.empty_count,cs.filled_count from consists as cs left join cylinder_type  as ct on ct.id = cs.cylinder_type_id where cs.inventory_id = {inventory_id};"
        result = self.db.exec(query=query)

        if result == None:
            return []

        data: list[tuple[str, int, int]] = []

        rows = result.fetchall()

        for row in rows:
            name = row.display_name
            empty_count = int(row.empty_count)
            filled_count = int(row.filled_count)

            data.append((name, empty_count, filled_count))

        return data

    # def getGasIncome(self, inventory_id: int) -> list[tuple[str, int, int]]:
    #     query: str = f"select ct.display_name,cs.cylinder_count, (cs.cylinder_count*ct.filled_gas_cylinder_exchange_price) as selling_income, (cs.cylinder_count*ct.cylinder_exchange_profit) as selling_profit  from encompass as cs join cylinder_type as ct on cs.cylinder_type_id=ct.id;"
    #     result = self.db.exec(query=query)

    #     if result == None:
    #         return []

    #     data: list[tuple[str, int]] = []

    #     rows = result.fetchall()

    #     for row in rows:
    #         name = row.display_name
    #         selling_income = int(row.selling_income)

    #         data.append((name, selling_income))

    #     return data

    def getLoanFinishedUnfinishedCount(self, previous_date: str) -> tuple[int, int]:
        query: str = f"select count(payment_id) as count_t,finished from loaned_payment where payment_id in (select id from payment where date_time > {previous_date} ) group by finished;"

        result = self.db.exec(query=query)

        if result == None:
            return (0, 0)

        rows = result.fetchall()

        unfinished_count = int(rows[0].count_t)
        finished_count = int(rows[1].count_t)

        return (unfinished_count, finished_count)

    def getGasIncomes(self) -> tuple[str, int, int]:
        query: str = f"select ct.display_name,cs.cylinder_count, (cs.cylinder_count*ct.filled_gas_cylinder_exchange_price) as selling_income, (cs.cylinder_count*ct.cylinder_exchange_profit) as selling_profit  from encompass as cs join cylinder_type as ct on cs.cylinder_type_id=ct.id;"

        result = self.db.exec(query=query)

        if result == None:
            return []

        data: list[tuple[str, int, int]] = []

        rows = result.fetchall()

        for row in rows:
            name = row.display_name
            selling_income = int(row.selling_income)
            selling_profit = int(row.selling_profit)

            data.append((name, selling_income, selling_profit))

        return data

    def getEmptySellingIncomeProfit(self) -> list[tuple[str, float, float]]:
        query: str = f"select ct.display_name, (cs.cylinder_count*ct.cylinder_selling_price) as selling_income, (cs.cylinder_count*ct.cylinder_selling_profit) as selling_profit  from comprises as cs join cylinder_type as ct on cs.cylinder_type_id=ct.id;"

        result = self.db.exec(query=query)

        if result is None:
            return []

        data: list[tuple[str, float, float]] = []

        rows = result.fetchall()

        for row in rows:
            cylinderName = row.display_name
            income = float(row.selling_income)
            profit = float(row.selling_profit)

            data.append((cylinderName, income, profit))

        return data

    def getEachManagerTransactionCount(self) -> list[tuple[str, int]]:
        query: str = f"select u.user_name,count(t.id) from manager as m left join transaction_t as t on t.manager_id = m.user_id left join user_t as u on m.user_id = u.id group by u.id,u.user_name;"

        result = self.db.exec(query=query)

        if result is None:
            return []

        data: list[tuple[str, int]] = []

        rows = result.fetchall()

        for row in rows:
            user_name = row[0]
            transaction_count = int(row[1])
            data.append((user_name, transaction_count))

        return data

    def getVehicleTransactionCounts(self) -> list[tuple[str, int]]:
        query: str = f"select dc.vehicle_number,count(rcst.customer_sale_transaction_id) as count_t from delivering_customer as dc left join registered_customer_sale_transaction as rcst on rcst.known_customer_id = dc.known_customer_id group by dc.vehicle_number order by count_t;"

        result = self.db.exec(query=query)

        if result is None:
            return []

        data: list[tuple[str, int]] = []

        rows = result.fetchall()

        for row in rows:
            vehicle_number = row.vehicle_number
            transaction_count = int(row.count_t)
            data.append((vehicle_number, transaction_count))

        return data

    def getUnFinishedLoanBalanceCountAll(self) -> int:
        query: str = f"select sum(total_loan_amount - current_paid_amount) as sumation from loaned_payment where finished = 0;"

        result = self.db.exec(query=query)

        if result is None:
            return 0

        row = result.fetchone()

        if row is None or row.sumation is None:
            return 0

        return int(row.sumation)

    def getRegAndUnregCustomerCounts(self) -> list[tuple[str, int]]:
        query: str = f"select 'registered' as type, count(*) as count_t from registered_customer_sale_transaction union all select 'anonymous' as type, count(*) as count_t from anonymous_customer_sale_transaction;"

        result = self.db.exec(query=query)

        if result is None:
            return []

        data: list[tuple[str, int]] = []

        rows = result.fetchall()

        for row in rows:
            customer_type = row.type
            count = int(row.count_t)
            data.append((customer_type, count))

        return data

    def getCylinderCountFromUserToGiveUs(self) -> int:
        query: str = f"select sum(given_cylinder_count - taken_cylinder_count) as counter from covers;"

        result = self.db.exec(query=query)

        if result is None:
            return 0

        row = result.fetchone()

        if row is None or row.counter is None:
            return 0

        return int(row.counter)

    def getSystemUsersHandledTransactionCount(self) -> list[tuple[int, str, int]]:
        query: str = f"select u.id,u.user_name,count(cst.id) from customer_sale_transaction as cst left join user_t as u on cst.user_id = u.id group by u.id,u.user_name;"

        result = self.db.exec(query=query)

        if result is None:
            return []

        data: list[tuple[int, str, int]] = []

        rows = result.fetchall()

        for row in rows:
            user_id = int(row.id)
            user_name = row.user_name
            transaction_count = int(row[2])

            data.append((user_id, user_name, transaction_count))

        return data

    def getCylinderTypeBySellCount(self) -> list[tuple[str, int]]:
        query: str = f"select ct.display_name,sum(cv.given_cylinder_count) from customer_sale_exchange_transaction as cset join covers as cv on cv.customer_sale_exchange_transaction_id = cset.customer_sale_transaction_id left join cylinder_type as ct on ct.id = cv.cylinder_type_id group by ct.id,ct.display_name;"

        result = self.db.exec(query=query)

        if result is None:
            return []

        data: list[tuple[str, int]] = []

        rows = result.fetchall()

        for row in rows:
            display_name = row.display_name
            total_given = int(row[1])
            data.append((display_name, total_given))

        return data

    def getActiveLoanAcount(self) -> int:
        query: str = "select count(payment_id) as ct from loaned_payment where finished =0;"

        result = self.db.exec(query=query)

        if result is None:
            return 0

        rows = result.fetchall()

        count = int(rows[0].ct)

        return count
