from database.db import Database


class BiDashboardRepository:

    def __init__(self, db: Database):
        self.db = db

    def getStock(self, inventory_id: int) -> tuple[str, int, int]:
        query: str = f"select ct.display_name,cs.empty_count,cs.filled_count from consists as cs left join cylinder_type  as ct on ct.id = cs.cylinder_type_id where cs.inventory_id = {inventory_id};"
        result = self.db.exec(query=query)

        if result == None:
            return None

        rows = result.fetchall()

        for row in rows:
            name = row.display_name
            empty_count = int(row.empty_count)
            filled_count = int(row.filled_count)

            return (name, empty_count, filled_count)

        return None
