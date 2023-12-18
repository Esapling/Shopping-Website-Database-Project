from database_manager import DatabaseManagement
import os
import psycopg
from cryptography.fernet import Fernet


class User(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="users")
        key = Fernet.generate_key()
        self.fkey = Fernet(key)

    def check_user_registered(self, in_user_data):
        email = in_user_data.email
        password = in_user_data.password
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                cur.execute("SELECT email, password from users")  # avoid sql injection
                user_data = cur.fetchall()
                if not user_data:
                    print("There is no user with given email pls check that")
                else:
                    password_in_db = self.fkey.decrypt(user_data.password)
                    if password == password_in_db:
                        return True
        return False

    def register_new_user(self, user):
        password = self.fkey.encrypt(user.password)
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                cur.execute = ("""INSERT INTO users (email, password, name, phone, address) values
                               (%s,%s,%s,%s,%s)""",
                               (user.email, password, user.name, user.phone, user.address))
            connection.commit()
