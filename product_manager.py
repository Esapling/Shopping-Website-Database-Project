from database_manager import DatabaseManagement
import psycopg


class Product(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="product")
        self.db_junction = DatabaseManagement(table_name="product")

    def getCategoryProducts(self, category_id: int):
        # get products' ids which belong to the given category from the product table
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query_junction = f"select * from product where category_id=%s"
                cur.execute(query_junction, (category_id,))
                products = cur.fetchall()
                # print(products)
                return products

    def getCategoryProductsWithLikes(self, category_id: int, customer_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                # select all products in the category with computed field "liked"
                # which is true if the product is in the customer's fav boxes
                # FIXME: Does this query work? --> All products are called
                query_junction = f"select product.*, case when product.product_id in " \
                                 f"(select product_id from customer_fav_boxes where customer_id=%s) " \
                                 f"then true else false end as liked from product where category_id=%s"
                cur.execute(query_junction, (customer_id, category_id,))
                products = cur.fetchall()
                # print(products)
                return products

    def getProductsWithName(self, string):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query = f"select * from product where product_name ILIKE %s" # ILIKE case insensitive while LIKE sensitive
                search_string = f"%{string}%"
                cur.execute(query, (search_string,))
                products = cur.fetchall()
                return products
    def sortProductPrices(self, opt):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                if opt.lower() in ('asc', 'desc'):
                    query = f"select * from product ORDER BY price {opt}"
                    cur.execute(query)
                    products = cur.fetchall()
                    return products
                else:
                    return None
                



class Category(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="CATEGORY")

    def getCategories(self):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query_junction = f"select * from category"
                cur.execute(query_junction)
                categories = cur.fetchall()
                # print(categories)
                return categories

    def getCategoryName(self, category_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query_junction = f"select category_name from category where category_id=%s"
                cur.execute(query_junction, (category_id,))
                category_name = cur.fetchone()
                # print(category_name)
                return category_name


class Store(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="STORE")

    def getStoreName(self, store_id: int):
        with psycopg.connect(**self.db_params) as connection:
            with connection.cursor() as cur:
                query_junction = f"select store_name from store where store_id=%s"
                cur.execute(query_junction, (store_id,))
                store_name = cur.fetchone()
                # print(store_name)
                return store_name

# if __name__ == '__main__':
#     db_product = Product()
#     #db_product.exectue_sqlscript("instances/products.sql")
#     #db_product.exectue_sqlscript("instances/store.sql")
#     #db_product.exectue_sqlscript("instances/product_junction.sql")
#     db_product.getCategoryProducts(category_id=1)
#         product_ids= [record[0] for record in records]
#         print(product_ids)
# #get product records from table
#         placeholders = '(' + ', '.join(['%s']*len(product_ids)) + ')'
#         query_products = f"SELECT * FROM product WHERE product_id IN {placeholders}"
#         #print(query_products)
#         cur.execute(query_products, (product_ids))
#         products = cur.fetchall()
