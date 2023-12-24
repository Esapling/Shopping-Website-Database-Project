-- look up table while searching for order details 
-- receipt table in other words
CREATE TABLE ORDER_JUNCTION (
    order_id INT REFERENCES PURCHASE_ORDER (order_id)
            ON DELETE CASCADE 
            ON UPDATE CASCADE, --is it possible for an order id to be changed ?? 

    product_id INT NOT NULL REFERENCES PRODUCT (product_id) 
            ON DELETE RESTRICT -- an order of which ordered products are not known ???
            ON UPDATE CASCADE,
    
    product_amount INT NOT NULL 
        CHECK (product_amount >= 0),  --cannot be larger than the inventory(stock) amount --trigger

    PRIMARY KEY (order_id, product_id)
);

--  order 1 includes product 1 amount of 2
--INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount, unit_product_price) VALUES (1,1, 2);
--order 1 includes product 2 amount of 3
-- INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (1,2, 3);
-- --order 1 includes product 3 amount 1INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (1,3, 1, 9.99);

-- -- so order 1 total of 2 + 3 + 1 products 
-- -- total order amount = 2*11 + 3*14 + 1*9.99

-- --  order 2 includes product 1 amount of 3
-- INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount, unit_product_price) VALUES (2,1, 3);
-- --order 2 includes product 2 amount of 1
-- INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount) VALUES (2,2, 1);
-- --order 2 includes product 3 amount 2
-- INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount) VALUES (2,3, 2);
-- --order 2 includes product 4 amount 4
-- INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount) VALUES (2,4, 4);

