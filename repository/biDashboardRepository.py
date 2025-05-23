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

    def getGasIncome(self, inventory_id: int) -> list[tuple[str, int, int]]:
        query: str = f"select ct.display_name,cs.cylinder_count, (cs.cylinder_count*ct.filled_gas_cylinder_exchange_price) as selling_income, (cs.cylinder_count*ct.cylinder_exchange_profit) as selling_profit  from encompass as cs join cylinder_type as ct on cs.cylinder_type_id=ct.id;"
        result = self.db.exec(query=query)

        if result == None:
            return []

        data: list[tuple[str, int]] = []

        rows = result.fetchall()

        for row in rows:
            name = row.display_name
            selling_income = int(row.selling_income)

            data.append((name, selling_income))

        return data

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