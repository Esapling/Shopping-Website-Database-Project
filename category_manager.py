from database_manager import DatabaseManagement
import os
import psycopg

class Category(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="category")

    def addCategory(self, category_name, store_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO {self.table_name} VALUES (%s,%s)"
                cur.execute(query, (category_name, store_id))
            connection.commit()

    def deleteCategory(self, category_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM {self.table_name} WHERE category_id=%s"
                cur.execute(query, category_id)
            connection.commit()

    def updateCategory(self, category_id, category_name,store_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"UPDATE {self.table_name} SET category_name=%s , store_id=%s  WHERE category_id=%s"
                cur.execute(query, (category_name,store_id,category_id))
            connection.commit()

    def findCategory(self, category_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT * FROM {self.table_name} WHERE category_id=%s" 
                cur.execute(query,(category_id))
                category = cur.fetchAll()
                if not category:
                    print("No category found with given Category Id")
                    return False
                else:
                    print("Category Found")
                    return category


    def findCategoryByStoreIdAndCategoryName(self, category_name, store_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT * FROM {self.table_name} WHERE category_name=%s AND store_id=%s" 
                cur.execute(query,(category_name, store_id))
                category = cur.fetchAll()
                if not category:
                    print("No category found with given parameters")
                    return False
                else:
                    print("Category Found")
                    return category

    def fetchAllCategories(self):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT * FROM {self.table_name}"
                cur.execute(query)
                category_list = cur.fetchAll()
                if not category_list:
                    print("No Categories Found in Database")
                    return False
                else:
                    print("Fetching Categories from Database is Successfull")
                    return category_list
