from database_manager import DatabaseManagement


class Store(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="store")
