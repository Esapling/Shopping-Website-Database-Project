import os
import psycopg


class DatabaseManagement:
    def __init__(self, table_name) -> None:
        # Database connection parameters
        self.table_name = None
        self.db_params = None
        self.dbname = None
        self.set_initials(table_name)

    def set_initials(self, table_name):
        self.dbname = os.environ['DB_NAME']  #
        self.db_params = {
            "dbname": self.dbname,
            "user": os.environ['DB_USERNAME'],  #
            "password": os.environ['DB_PASS']  #
        }

        self.table_name = table_name

    def execute_sqlscript(self, sql_file_path):
        with open(file=sql_file_path, mode="r") as sqlfile:
            sql_script_commands = sqlfile.read()
            print(sql_script_commands)
            print("File read success")
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                cur.execute(sql_script_commands)
                connection.commit()

    def getById(self, id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"select * from {self.table_name} where {self.table_name}_id = %s"  # table_name_id
                # ex: category_id for each design
                # see the seperated classes for specific designs

                cur.execute(query, (id,))  # avoid sql injection!
                data = cur.fetchone()
                return data

    def deleteByID(self, id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM {self.table_name} where {self.table_name}_id = %s;"
                cur.execute(query, (id,))  # avoid sql injection!

    def getRecords(self):
        print(self.table_name)
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT * from {self.table_name}"
                cur.execute(query)
                data = cur.fetchall()
                return data


if __name__ == "__main__":
    db = DatabaseManagement("customer")

    # db.execute_sqlscript("instances/is_registered_flag_trigger.sql")
    # db.execute_sqlscript("instances/inventory_provider.sql")

    # db.execute_sqlscript("instances/store.sql")
    # db.execute_sqlscript("instances/categories.sql")
    # db.execute_sqlscript("instances/customer.sql")
    # db.execute_sqlscript("instances/products.sql")
    # db.execute_sqlscript("instances/order.sql")
    # db.execute_sqlscript("instances/order_junction.sql")
    # db.execute_sqlscript("instances/category_trigger.sql")
    # db.execute_sqlscript("instances/price_trigger_delete.sql")
    # db.execute_sqlscript("instances/price_trigger_insert.sql")

    # db.execute_sqlscript("instances/shop_box.sql")
    # db.execute_sqlscript("instances/fav_box.sql")

    # db = DatabaseManagement("customer")
    #
    # db.execute_sqlscript("instances/price_trigger.sql")
    # x = db.getById(4)
    # print(x)
