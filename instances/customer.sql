CREATE TABLE CUSTOMER(
    customer_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL ,
    phone VARCHAR(100) NOT NULL UNIQUE, -- phone numbers must belong to only one person 
    customer_address  VARCHAR(100) NOT NULL,
    is_registered BOOLEAN DEFAULT FALSE;
);
