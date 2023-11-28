CREATE TABLE PRODUCT(
    product_id SERIAL PRIMARY KEY NOT NULL, 
    product_name VARCHAR(100) NOT NULL ,

    inventory INT DEFAULT 0 NOT NULL
        CHECK (inventory >= 0),
    
    price FLOAT NOT NULL 
        CHECK (price >= 0),

    category_id INT REFERENCES CATEGORY (category_id) 
            --ON DELETE SET NULL 
            ON DELETE RESTRICT
            ON UPDATE CASCADE,
    
    store_id INT REFERENCES STORE (store_id)
             --ON DELETE SET NULL 
             ON DELETE RESTRICT
             ON UPDATE CASCADE

);

