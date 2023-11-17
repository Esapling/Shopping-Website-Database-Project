CREATE TABLE ORDER (
    order_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    order_state BOOLEAN DEFAULT FALSE -- declares if order is received by the user
    order_date TIMESTAMP(0) NOT NULL DEFAULT current_timestamp(0),
    --total price ????s

);


-- no need to add anythin by hand

INSERT INTO ORDER_JUNCTION (order_state) VALUES (FALSE);

-- order belongs to customer 1 - order is being prepared (FALSE) - now 
--INSERT INTO ORDER_JUNCTION (customer_id) VALUES (1);
-- order belongs to customer 2 - order is being prepared (FALSE) - now 
--INSERT INTO ORDER_JUNCTION (customer_id) VALUES (1);
