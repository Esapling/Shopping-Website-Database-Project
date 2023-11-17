create table CATEGORY (
	category_id SERIAL PRIMARY KEY NOT NULL UNIQUE,
	category_name VARCHAR(50) UNIQUE NOT NULL,
    --products INT[10] FOREIGN KEY references products (product_id) 
);
insert into CATEGORY (category_id, category_name) values (1, 'Electronics');
insert into CATEGORY (category_id, category_name) values (2, 'Grocery');
insert into CATEGORY (category_id, category_name) values (3, 'Automotive');
insert into CATEGORY (category_id, category_name) values (4, 'Kids');
insert into CATEGORY (category_id, category_name) values (5, 'Health');
insert into CATEGORY (category_id, category_name) values (6, 'Clothing');
insert into CATEGORY (category_id, category_name) values (7, 'Home');
insert into CATEGORY (category_id, category_name) values (8, 'Books');
insert into CATEGORY (category_id, category_name) values (9, 'Industrial');

-- insert into CATEGORY (category_id, category_name) values (14, 'Games');
-- insert into CATEGORY (category_id, category_name) values (15, 'Jewelry');
-- insert into CATEGORY (category_id, category_name) values (7, 'Shoes');
-- insert into CATEGORY (category_id, category_name) values (7, 'Shoes');
-- insert into CATEGORY (category_id, category_name) values (7, 'Garden');

