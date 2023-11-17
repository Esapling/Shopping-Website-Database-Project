-- look up to this table while searching for item in a shop or in a category
-- be careful while querying and about data integrity
CREATE TABLE PRODUCT_JUNCTION (
    product_id INT NOT NULL UNIQUE references PRODUCT (product_id)
            ON DELETE CASCADE 
            ON UPDATE CASCADE,

    category_id INT NOT NULL REFERENCES CATEGORY (category_id) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE,
            
    
    store_id INT NOT NULL REFERENCES STORE (store_id) 
            ON DELETE CASCADE 
            ON UPDATE CASCADE,
    
    PRIMARY KEY (product_id, category_id, store_id)
);

INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (1,1,1); --laptop
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (2,1,1); --phone
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (3,1,1); --computer
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (4,1,1); --ipad
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (5,1,1); --airpods
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (6,1,2);
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (7,1,2);
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (8,1,2);
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (9,1,2);
INSERT INTO PRODUCT_JUNCTION (product_id, category_id, store_id) VALUES (10,1,2);

