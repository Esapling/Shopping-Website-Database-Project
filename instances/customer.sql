CREATE TABLE CUSTOMER(
    customer_id SERIAL PRIMARY KEY NOT NULL,
    customer_name VARCHAR(100) NOT NULL ,
    customer_phone VARCHAR(100) NOT NULL UNIQUE, -- phone numbers must belong to only one person 
    customer_address  VARCHAR(100) NOT NULL,
    is_registered BOOLEAN DEFAULT FALSE,
    customer_email VARCHAR(100) UNIQUE,
    customer_password VARCHAR(100)
);

