create table STORE(
                      store_id SERIAL UNIQUE PRIMARY KEY NOT NULL,
                      phone VARCHAR(50) UNIQUE,
                      location VARCHAR(50) UNIQUE
);

create table CATEGORY (
	category_id SERIAL PRIMARY KEY NOT NULL UNIQUE,
	category_name VARCHAR(50) UNIQUE NOT NULL,
	store_id INT,
	FOREIGN KEY (store_id) REFERENCES STORE (store_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);
CREATE TABLE CUSTOMER(
                         customer_id SERIAL PRIMARY KEY NOT NULL,
                         customer_name VARCHAR(100) NOT NULL ,
                         customer_phone VARCHAR(100) NOT NULL UNIQUE, -- phone numbers must belong to only one person
                         customer_address  VARCHAR(100) NOT NULL,
                         is_registered BOOLEAN DEFAULT FALSE,
                         customer_email VARCHAR(100) UNIQUE, -- also email must belong to only one person
                         customer_password VARCHAR(100)
);
CREATE TABLE PRODUCT(
                        product_id SERIAL PRIMARY KEY NOT NULL,
                        product_name VARCHAR(100) NOT NULL ,

                        inventory INT DEFAULT 0 NOT NULL
                            CHECK (inventory >= 0),

                        price FLOAT NOT NULL
                            CHECK (price >= 0),

                        category_id INT REFERENCES CATEGORY (category_id)
                            ON DELETE RESTRICT
                            ON UPDATE CASCADE,

                        store_id INT REFERENCES STORE (store_id)
                            ON DELETE RESTRICT
                            ON UPDATE CASCADE

);
CREATE TABLE PURCHASE_ORDER(
                   order_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
                   customer_id INT NOT NULL REFERENCES customer (customer_id)
                       ON DELETE SET NULL
                       ON UPDATE CASCADE,
                   order_state BOOLEAN DEFAULT FALSE, -- shows if order is reached to the customer, simply order is done
                   order_date TIMESTAMP(0) DEFAULT current_timestamp(0),
                   total_price DOUBLE PRECISION DEFAULT 0
                       check (total_price >= 0)
);
CREATE TABLE ORDER_JUNCTION (
                        order_id INT REFERENCES PURCHASE_ORDER (order_id)
                            ON DELETE CASCADE
                            ON UPDATE CASCADE, -- if order is deleted, ordered products are also deleted

                        product_id INT NOT NULL REFERENCES PRODUCT (product_id)
                            ON DELETE RESTRICT -- if product is deleted, ordered product is not deleted
                            ON UPDATE CASCADE,

                        product_amount INT NOT NULL
                            CHECK (product_amount >= 0), --cannot be larger than the inventory(stock) amount --trigger

                        PRIMARY KEY (order_id, product_id)
);
CREATE TABLE CUSTOMER_SHOP_BOX(
                      box_id SERIAL PRIMARY KEY  NOT NULL,
                      customer_id INT REFERENCES CUSTOMER (customer_id)
                          ON DELETE CASCADE
                          ON UPDATE CASCADE,

                      product_id INT NOT NULL REFERENCES PRODUCT (product_id)
                          ON DELETE CASCADE
                          ON UPDATE CASCADE
);
CREATE TABLE CUSTOMER_FAV_BOXES(
                       box_id SERIAL NOT NULL,
                       customer_id INT REFERENCES CUSTOMER (customer_id)
                           ON DELETE CASCADE
                           ON UPDATE CASCADE,

                       product_id INT NOT NULL REFERENCES PRODUCT (product_id)
                           ON DELETE CASCADE
                           ON UPDATE CASCADE,
                       PRIMARY KEY (customer_id, product_id)
);

