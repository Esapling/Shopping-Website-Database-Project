CREATE TABLE CUSTOMER_FAV_BOXES(
    box_id SERIAL PRIMARY KEY NOT NULL,
    customer_id INT REFERENCES CUSTOMER (customer_id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    product_id INT NOT NULL REFERENCES PRODUCT (product_id) 
            ON DELETE CASCADE -- you missed the possiblity of buying the relevan item sadly :)
            ON UPDATE CASCADE,
);
