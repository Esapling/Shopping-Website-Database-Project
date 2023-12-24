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

    # NOTE: Not used
    def getItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT product_id from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products

    def searchItem(self, customer_id: int, product_id: int):
        x = None
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT 1 from {self.table_name} where customer_id = %s AND product_id = %s"
                cur.execute(query, (customer_id, product_id))
                x = cur.fetchone()
        return x


class ShopBox(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="CUSTOMER_SHOP_BOX")

    # NOTE: Not used
    def addItemToShopBox(self, customer_id: int, product_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO {self.table_name} (customer_id, product_id) VALUES (%s, %s)"
                cur.execute(query, (customer_id, product_id))
            connection.commit()

    # NOTE: Not used
    def getItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT product_id from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products

    def searchItemInCart(self, customer_id, product_id):
        item_exist = False
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT 1 from {self.table_name} where customer_id = %s AND product_id = %s"
                cur.execute(query, (customer_id, product_id))
                item_exist = cur.fetchone()
            return item_exist

    def remove_from_cart(self, customer_id, product_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM {self.table_name} where customer_id = %s AND product_id = %s"
                cur.execute(query, (customer_id, product_id))
            connection.commit()


class Order(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="PURCHASE_ORDER")

    """
    def addOrder(self, customer_id: int, product_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"INSERT INTO {self.table_name} (customer_id, order_id) VALUES (%s, %s)"
                cur.execute(query, (customer_id, product_id))
            connection.commit()

    def getItems(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"SELECT order_id from {self.table_name} where customer_id = %s"
                cur.execute(query, (customer_id,))
                products = cur.fetchall()
        return products
    """

    # Get all individual item orders history of a customer using order_junction table
    def getCustomerOrderHistory(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                # (Important) List orders as a list of dictionaries containing
                #   order information (total cost, order date,...) as titles
                #   and more details (product names, individual prices, etc.) as info-items
                #  OR...
                #  --> Simply list all purchased products and their prices with order date and numbers for customer
                # Listing: order no, order date, total price(?), product name, unit price, product amount
                query = """SELECT o.order_id AS Order_No, o.order_date AS Date, o.total_price AS Order_total_cost, 
                            p.product_name AS Name, p.price, oj.product_amount AS Amount_bought
                            FROM purchase_order o 
                            LEFT JOIN order_junction oj ON o.order_id = oj.order_id 
                            LEFT JOIN product p ON oj.product_id = p.product_id 
                            WHERE o.customer_id = %s 
                            ORDER BY o.order_date DESC, o.order_id DESC"""
                cur.execute(query, (customer_id,))
                order_history = cur.fetchall()
        return order_history

    def createOrder(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                # Get products from customer_shop_box for given customer
                # on condition of all product fulfilling condition: inventory > requested
                # Cart view
                view_name_c = 'customer_shop_box_view'
                query = (f"CREATE OR REPLACE VIEW {view_name_c} AS "
                         f"(SELECT csb.product_id, p.product_name, p.inventory, p.price from customer_shop_box csb "
                         f"left join product p on csb.product_id = p.product_id where csb.customer_id = {customer_id})")
                cur.execute(query)

                # Handle the case where the cart is empty
                query = f"SELECT COUNT(*) from {view_name_c}"
                cur.execute(query)
                cart_size = cur.fetchone()[0]
                if cart_size == 0:
                    connection.close()
                    return None, False

                # Purchase view
                view_name_p = 'purchase_view'
                query = (f"CREATE OR REPLACE VIEW {view_name_p} AS "
                         f"(SELECT COUNT(v.product_id) AS count, v.product_id AS product_id, v.price AS price "
                         f"FROM {view_name_c} AS v GROUP BY v.product_id, v.price)")
                cur.execute(query)

                # Check if stock is available for all products in the cart --> supply >= demand
                query = (f"SELECT COUNT(s.product_id), SUM(s.price) from {view_name_c} s left join {view_name_p} d "
                         f"on s.product_id = d.product_id where s.inventory >= d.count")
                cur.execute(query)
                num_in_stock, total_price = cur.fetchone()

                # Handle the case where a product stock is not enough
                # Stock is not available for at least one product
                if num_in_stock < cart_size:  # total_price[0][0] is None:
                    # Find the products that are out of stock to inform the user
                    query = (f"SELECT DISTINCT s.product_name from {view_name_c} s join {view_name_p} d "
                             f"on s.product_id = d.product_id where s.inventory < d.count")
                    cur.execute(query)
                    out_of_stock_products = cur.fetchall()
                    connection.close()
                    return out_of_stock_products, False
                # Stock is available for all products
                else:
                    # Decrease inventory by the number of products bought
                    query = (f"UPDATE product AS p SET inventory = p.inventory - sq.count FROM "
                             f"{view_name_p} AS sq WHERE sq.product_id = p.product_id")
                    cur.execute(query)
                    # Insert order into customer_orders table, with total price
                    # (Order state is true for now, it will be updated only after the order is delivered)
                    query = (f"INSERT INTO {self.table_name} (customer_id, order_state, total_price) "
                             f"VALUES (%s, true, %s) RETURNING order_id")
                    cur.execute(query, (customer_id, total_price))

                    # Get the last inserted ID
                    last_inserted_order_id = cur.fetchone()[0]
                    # Record items bought to order_junction table using latest purchase_order
                    query = (f"INSERT INTO order_junction (order_id, product_id, product_amount) "
                             f"SELECT o.order_id,v.product_id,v.count as product_amount "
                             f"FROM {view_name_p} AS v LEFT JOIN purchase_order AS o "
                             f"ON o.order_id = {last_inserted_order_id} RETURNING order_id")
                    cur.execute(query)

                    # Remove bought products from customer_shop_box
                    query = f"DELETE FROM customer_shop_box WHERE customer_id = %s"
                    cur.execute(query, (customer_id,))

            connection.commit()
            connection.close()
            return None, True


class Customer(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="customer")

    def registerCustomer(self, customer_id: int, email, password):

        # hash the given password and keep the hashed result in the db
        hashed_password = hashPassword(password=password)

        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = (f"UPDATE {self.table_name} SET customer_email = %s, customer_password = %s "
                         f"where customer_id = %s")
                cur.execute(query, (email, hashed_password, customer_id))
            connection.commit()
            connection.close()

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
            connection.close()

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
                if is_registered_tuple[0]:
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
            connection.close()

    def emptyCart(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"DELETE FROM customer_shop_box WHERE customer_id = %s"
                cur.execute(query, (customer_id,))
            connection.commit()
            connection.close()

    # login
    def validateCustomerRegistered(self, email_addr, password):
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
                # Check if email or phone number is already taken
                query = f"SELECT customer_id from {self.table_name} where customer_email = %s or customer_phone = %s"
                cur.execute(query, (customer_dict['email'], customer_dict['phone']))
                customer = cur.fetchone()
                if customer is not None:
                    # if the customer id is not the same as the given id, then it is a different customer
                    if customer[0] != customer_id:
                        connection.close()
                        return False
                    # Update customer info
                    else:
                        query = f"""UPDATE {self.table_name} SET customer_name = %s, customer_phone = %s, customer_address = %s,
                        customer_email = %s where customer_id = %s"""
                        cur.execute(query, (customer_dict['name'], customer_dict['phone'], customer_dict['address'],
                                            customer_dict['email'], customer_id))
                        connection.commit()
                        connection.close()
                        return True

    def deleteCustomer(self, customer_id):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"""DELETE FROM {self.table_name} WHERE customer_id = %s"""
                cur.execute(query, (customer_id,))
            connection.commit()
            connection.close()
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
