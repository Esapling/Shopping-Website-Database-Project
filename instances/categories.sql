create table CATEGORY (
	category_id SERIAL PRIMARY KEY NOT NULL UNIQUE,
	category_name VARCHAR(50) UNIQUE NOT NULL,
	store_id INT,
	FOREIGN KEY (store_id) REFERENCES STORE (store_id) -- is this really necessary
             --ON DELETE SET NULL 
            ON DELETE CASCADE
            ON UPDATE CASCADE
);
insert into CATEGORY (category_name,store_id) values ('Electronics',1);
insert into CATEGORY (category_name,store_id) values ('Grocery',1);
insert into CATEGORY (category_name,store_id) values ('Automotive',1);
insert into CATEGORY (category_name,store_id) values ('Kids',1);
insert into CATEGORY (category_name,store_id) values ('Health',1);
insert into CATEGORY (category_name,store_id) values ('Clothing',1);
insert into CATEGORY (category_name,store_id) values ('Home',1);
insert into CATEGORY (category_name,store_id) values ('Books',1);
insert into CATEGORY (category_name,store_id) values ('Industrial',1);

-- insert into CATEGORY (category_id, category_name) values (14, 'Games');
-- insert into CATEGORY (category_id, category_name) values (15, 'Jewelry');
-- insert into CATEGORY (category_id, category_name) values (7, 'Shoes');
-- insert into CATEGORY (category_id, category_name) values (7, 'Shoes');
-- insert into CATEGORY (category_id, category_name) values (7, 'Garden');

