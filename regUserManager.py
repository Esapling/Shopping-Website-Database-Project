import psycopg
from database_manager import DatabaseManagement
from utilities import HasH


class RegUser(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="registered_user")

    def getUserDetails(self, email_addr, password):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"select * from {self.table_name} where email = %s and password = %s"
                cur.execute(query, (email_addr, password))
                user = cur.fetchone()
                if user is None:
                    print("NO USER IS FOUND WITH GIVEN EMAIL AND PASS")
                    return False
                else:
                    print(f"WELCOME {user}")
                    return True

    def insert(self, user_tuple):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                hasher = HasH()
                hashed_password = hasher.hash(user_tuple[3])
                query = f"INSERT INTO registered_user VALUES (%s, %s, %s, %s, %s)"
