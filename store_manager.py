from database_manager import DatabaseManagement

# Note: Not  used at the moment.

class Store(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="store")
