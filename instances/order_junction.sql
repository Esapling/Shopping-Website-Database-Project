-- look up to this table while searching for item in a shop or in a category
-- be careful while querying and about data integrity
-- receipt table in other words
CREATE TABLE ORDER_JUNCTION (
    order_id INT REFERENCES ORDER (order_id)
            ON DELETE CASCADE 
            ON UPDATE CASCADE, --can it be possible for an order id to be changed ?? 

    customer_id INT NOT NULL FOREIGN KEY REFERENCES CUSTOMER 
        ON DELETE SET NULL  --even if the user records deleted from the server
                            -- we might want to keep just previous oreders for our sake
        ON UPDATE CASCADE  ,


    product_id INT NOT NULL REFERENCES STORE (store_id) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE,
    
    product_amount INT NOT NULL 
        CHECK (product_amount >= 0),  --cannot be larger than the inventory(stock) amount

    PRIMARY KEY (product_id, customer_id, product_id)
);

--  order 1 includes product 1 amount of 2 by customer 1
INSERT INTO ORDER_JUNCTION (order_id, customer_id, product_id, product_amount) VALUES (1,1, 2, 1);
 
--order 1 includes product 2 amount of 3 by customer 1
INSERT INTO ORDER_JUNCTION (order_id, customer_id, product_id, product_amount) VALUES (1,1, 3, 2);

--order 1 includes product 3 amount 1 by customer 1
INSERT INTO ORDER_JUNCTION (order_id, customer_id, product_id, product_amount) VALUES (1,1, 1, 3);

-- so order 1 total of 2 + 3 + 1 products by customer 1 
