CREATE TABLE PRODUCT(
    product_id SERIAL PRIMARY KEY NOT NULL, 
    product_name VARCHAR(100) NOT NULL ,

    -- store_id INT REFERENCES STORES (store_id) 
    --         ON DELETE CASCADE 
    --         ON UPDATE CASCADE,
    
    -- category_id INT REFERENCES CATEGORIES (category_id) 
    --         ON DELETE CASCADE 
    --         ON UPDATE CASCADE,

    inventory INT DEFAULT 0 NOT NULL
        CHECK (inventory >= 0),
    
    price FLOAT NOT NULL 
        CHECK (price >= 0)
);

INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Laptop',   50,  1000);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Phone',    50,  250);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Computer', 50,  899);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Ipad',     50,  450);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Airpods',  50,  150);

INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Laptop',   50,  1499);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Phone',    50,  450);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Computer', 50,  630);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Ipad',     50,  430);
INSERT INTO PRODUCT (product_name, inventory, price) VALUES ('Airpods',  50,  100);
