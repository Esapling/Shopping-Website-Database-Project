from database_manager import DatabaseManagement
import psycopg

class Product(DatabaseManagement):
    def __init__(self) -> None:
        super().__init__(table_name="product")
        self.db_junction = DatabaseManagement(table_name="product")

    def getCategoryProducts(self, category_id: int):
        #get products' ids which belong to the given category from the product table
        with psycopg.connect(**self.db_params)as connection:
            with connection.cursor() as cur:
                query_junction = f"select * from product where category_id=%s"
                cur.execute(query_junction, (category_id,))
                products= cur.fetchall()
                #print(products)
                return products


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
