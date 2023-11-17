import os
import psycopg

class DatabaseManagement:
    def __init__(self, table_name) -> None:
    # Database connection parameters
        self.set_initials(table_name)


    def set_initials(self, table_name):
        self.dbname= os.environ['DB_NAME']
        self.db_params = {
            "dbname":self.dbname,
            "user":os.environ['DB_USERNAME'],
            "password":os.environ['DB_PASS']
        }
        
        self.table_name = table_name

    def exectue_sqlscript(self , sql_file_path):
        with open(file=sql_file_path, mode="r") as sqlfile:
                    sql_script_commands = sqlfile.read()
                    print(sql_script_commands)
                    print("File read success")
        with psycopg.connect(**self.db_params)as connection:
            with connection.cursor() as cur:
                    cur.execute(sql_script_commands)
                    connection.commit()

    def getById(self,id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"select * from {self.table_name} where {self.table_name}_id = %s"  #table_name_id 
                                                                        # ex: category_id for each design
                                                                        #see the seperated classes for specific designs
                
                cur.execute(query,(id,)) #avoid sql injection!
                data = cur.fetchone()
                return data
    
    def deleteByID(self, id: int):
        with psycopg.connect(**self.db_params)as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM {self.table_name} where {self.table_name}_id = %s;" 
                cur.execute(query, (id,)) #avoid sql injection!
        
    def getRecords(self):
        print(self.table_name)
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT * from {self.table_name}"
                cur.execute(query)
                data = cur.fetchall()
                return data
    
