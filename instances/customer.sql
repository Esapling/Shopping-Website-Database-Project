--check if customer is an CUSTOMER -> no need to save ???
CREATE TABLE CUSTOMER(
    customer_id SERIAL PRIMARY KEY NOT NULL,
    fullname VARCHAR(100) NOT NULL ,
    phone VARCHAR(100) NOT NULL ,
    loc_address  VARCHAR(100) NOT NULL,
    --registered_user BOOLEAN DEFAULT FALSE NOT NULL
);


insert into CUSTOMER (customer_id, fullname, phone, password) values (15, 3, 'Rosella','404-668-0698', 'rjenkine@ted.com',       );
insert into CUSTOMER (customer_id, fullname, phone, password) values (16, 13, 'Tomas', '404-668-0698','tbarmef@dailymail.co.uk', );
insert into CUSTOMER (customer_id, fullname, phone, password) values (17, 6, 'Catharina''404-668-0698', 'cespinozag@cdc.gov',  );
insert into CUSTOMER (customer_id, fullname, phone, password) values (18, 18, 'Dudley','404-668-0698', 'dwesthoferh@yolasite.com');
