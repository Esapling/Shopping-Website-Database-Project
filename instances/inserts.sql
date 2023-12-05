
--These inserst are already done for testing purposes
insert into CUSTOMER (name, phone, customer_address) values ('Rosella','404-668-0698', '82 Reindahl Point');
insert into CUSTOMER (name, phone, customer_address) values ('Tomas', '404-668-0690','6006 Luster Junction');
insert into CUSTOMER (name, phone, customer_address) values ('Catharina','404-668-0691','72 Cascade Point');
insert into CUSTOMER (name, phone, customer_address) values ('Dudley','404-668-0692','065 Fremont Plaza' );
insert into CUSTOMER (name, phone, customer_address) values ('fidan','444-44-0000', '34453 Ayagaza Bee Gate');

insert into registered_user (customer_id, email, password) values (5,'fidan20@itu.edu.tr' , 'passwordtest');

insert into PURCHASE_ORDER(customer_id, order_state) VALUES (1, FALSE);
insert into PURCHASE_ORDER(customer_id, order_state) VALUES (2, FALSE);
insert into PURCHASE_ORDER(customer_id, order_state) VALUES (3, FALSE);

--  order 1 includes product 1 amount of 2
INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount, unit_product_price) VALUES (1,1, 2, 11);
--order 1 includes product 2 amount of 3
INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (1,2, 3, 14);
--order 1 includes product 3 amount 1INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (1,3, 1, 9.99);
-- -- so order 1 total of 2 + 3 + 1 products 
-- -- total order amount = 2*11 + 3*14 + 1*9.99

--  order 2 includes product 1 amount of 3
INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount, unit_product_price) VALUES (2,1, 3, 15);
--order 2 includes product 2 amount of 1
INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (2,2, 1, 12);
-- --order 2 includes product 3 amount 2
INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (2,3, 2, 10);
-- --order 2 includes product 4 amount 4
INSERT INTO ORDER_JUNCTION (order_id, product_id, product_amount,unit_product_price) VALUES (2,4, 4, 11.50);

