CREATE TABLE PURCHASE_ORDER(
    order_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customer (customer_id) 
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    order_state BOOLEAN DEFAULT FALSE, -- shows if order is reached to the customer, simply order is done,
    order_date TIMESTAMP(0) DEFAULT current_timestamp(0),
    total_price DOUBLE PRECISION DEFAULT 0
        check (total_price >= 0) 
);
-- while adding a new customer first add the customer to the related table 
-- then add the order info 
-- consider possible error, for that need a trigger to check if the given customer exists
-- but customer table does not keep the registered customers
-- it only depends of the ordered orders
-- so its natural to create (if not exists) a record in the customer table and then in the order table


