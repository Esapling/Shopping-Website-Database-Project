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
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Phone',    50,  250,1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Computer', 50,  899, 1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Ipad',     50,  450, 1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Airpods',  50,  50,  1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Laptop',   50,  1499,1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Phone',    50,  450, 1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Computer', 50,  630, 1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Ipad',     50,  430, 1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Airpods',  50,  100, 1,1);
INSERT INTO PRODUCT (product_name, inventory, price,category_id, store_id) VALUES ('Laptop',   50,  1299,1,1);
    
    

