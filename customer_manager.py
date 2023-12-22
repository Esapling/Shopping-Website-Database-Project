import psycopg
from database_manager import DatabaseManagement

from utilities import hashPassword, verifyPassword


class FavBox(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="CUSTOMER_FAV_BOXES")

    def addItemToFavBox(self, customer_id: int, product_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO {self.table_name} (customer_id, product_id) VALUES (%s, %s)"
                cur.execute(query, (customer_id, product_id))

            connection.commit()

    def removeItemFromFavBox(self, customer_id: int, product_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM {self.table_name} WHERE customer_id = %s AND product_id = %s"
                cur.execute(query, (customer_id, product_id))

            connection.commit()

    def getItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT product_id from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products


class ShopBox(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="CUSTOMER_SHOP_BOX")

    def addItemToShopBox(self, customer_id: int, product_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO {self.table_name} (customer_id, product_id) VALUES (%s, %s)"
                cur.execute(query, (customer_id, product_id))
            connection.commit()

    def getItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT product_id from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products


class Order(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="CUSTOMER_ORDERS")

    def addOrder(self, customer_id: int, product_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO {self.table_name} (customer_id, product_id) VALUES (%s, %s)"
                cur.execute(query, (customer_id, product_id))
            connection.commit()

    def getItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT product_id from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products

class Customer(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="customer")

    def registerCustomer(self, customer_id: int, email, password):

        # hash the given password and keep the hashed result in the db
        hashed_password = hashPassword(password=password)

        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"UPDATE {self.table_name} SET customer_email = %s, customer_password = %s where customer_id = %s"
                cur.execute(query, (email, hashed_password, customer_id))
            connection.commit()

    def addCustomer(self, customer_dict):
        """ 
            Inserts new customer record into customer table
        """
        hashed_password = hashPassword(password=customer_dict['password'])  # hash given password and store it instead

        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"""INSERT INTO {self.table_name} 
                (customer_name, customer_phone, customer_address, is_registered, customer_email, customer_password) 
                VALUES (%s, %s, %s, %s, %s,%s)"""
                cur.execute(query,
                            (customer_dict['name'], customer_dict['phone'], customer_dict['address'], True,
                             customer_dict['email'], hashed_password))
            connection.commit()

    def checkCustomerRegisteredById(self, customer_id: int):
        """
            Returns True if the customer with given id is already registered,
            False otherwise
        """
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT is_registered FROM {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                is_registered_tuple = cur.fetchone()  # returned object is tuple
                if is_registered_tuple[0] == True:
                    return True
                else:
                    return False

    # signup
    def checkCustomerExistByPhone(self, customer_phone):
        """
            Checks a matching customer exists with the given customer phone
            if so returns the customer id 
            otherwise returns None
        """
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT customer_id from {self.table_name} where customer_phone = %s"
                cur.execute(query, (customer_phone,))
                customer = cur.fetchone()
                if customer is None:
                    return None
                else:
                    return customer[0]  # customer tuple object[0] - id value

    def getCustomerIdByEmail(self, customer_email):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT customer_id from {self.table_name} where customer_email = %s"
                cur.execute(query, (customer_email,))
                customer = cur.fetchone()
                if customer is None:
                    return None
                else:
                    return customer[0]  # customer tuple object[0] - id value

    def getCartItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT p.* from customer_shop_box csb left join" \
                        f" product p on csb.product_id = p.product_id where csb.customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products

    def addItemToCart(self, customer_id, product_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO customer_shop_box (customer_id, product_id) VALUES (%s, %s)"
                cur.execute(query, (customer_id, product_id))
            connection.commit()

    def emptyCart(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM customer_shop_box WHERE customer_id = %s"
                cur.execute(query, (customer_id,))
            connection.commit()

    # login
    def validataCustomerRegistered(self, email_addr, password):
        """
            returns customer data if a customer with given email and password found in the system,
            None otherwise
        """

        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"select customer_password from {self.table_name} where customer_email = %s"
                cur.execute(query, (email_addr,))
                user = cur.fetchone()
                if user is None:
                    print("NO USER IS FOUND WITH GIVEN EMAIL")
                    return None
                else:
                    # verify given password is correct
                    isValid = verifyPassword(password=password, hashed_pass=user[0])
                    if isValid:
                        return True
                    else:
                        return False

    def getCustomerByEmail(self, email):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"select customer_name, customer_phone, customer_address, customer_email, customer_id from {self.table_name} where customer_email = %s"
                cur.execute(query, (email,))
                customer = cur.fetchone()
                return customer

    def isCustomerRegistered(self, customer_id: int):
        """
            Checks if customer with given ID registered to the system, 
            if so returns true 
            False otherwise
        """
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT is_registered from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                is_registered = cur.fetchone()
                return is_registered

    # Update customer, For empty fields, it will keep the old values.
    def updateCustomer(self, customer_id, customer_dict):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"""UPDATE {self.table_name} SET customer_name = %s, customer_phone = %s, customer_address = %s,
                 customer_email = %s where customer_id = %s"""
                cur.execute(query, (customer_dict['name'], customer_dict['phone'], customer_dict['address'],
                                    customer_dict['email'], customer_id))
            connection.commit()

    def deleteCustomer(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"""DELETE FROM {self.table_name} WHERE customer_id = %s"""
                cur.execute(query, (customer_id,))
            connection.commit()
            print('G\'bye world')


    # def getCustomerIdByEmail(self, email):
    #     """ This method returns None if no user exists with given email
    #         otherwise returns customer id of the searched user
    #     """
    #     with psycopg.connect(**self.db_params)as connection:
    #         with connection.cursor() as cur:
    #             query = f"select 1 from customer where email = %s"
    #             cur.execute(query, (email,))
    #             user_found = cur.fetchone()
    #             if user_found:
    #                 return True
    #             else:
    #                 return False



