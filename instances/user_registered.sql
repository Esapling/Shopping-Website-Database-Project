CREATE TABLE registered_user(
    registered_user_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    customer_id INT DEFAULT 0 -- user information must first saved into customer table 
        REFERENCES CUSTOMER (customer_id)
             --ON DELETE SET NULL 
            ON DELETE SET NULL
            ON UPDATE CASCADE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL UNIQUE
);
