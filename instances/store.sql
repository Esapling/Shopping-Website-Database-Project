create table STORE(
	store_id SERIAL UNIQUE PRIMARY KEY NOT NULL,
	phone VARCHAR(50) UNIQUE,
	location VARCHAR(50) UNIQUE
);
insert into store (phone, location) values ('926-860-2750', '9869 Golf Course Place');
insert into store (phone, location) values ('270-616-0688', '82 Reindahl Point');

-- insert into STORE (store_id, categories,) values (2, [10,10,10], '270-616-0688', '82 Reindahl Point');
-- insert into STORE (store_id, categories ) values (3, [12,12,12,12,12,12,12,12,12,12], '154-844-2242', '6006 Luster Junction');
-- insert into STORE(store_id, categories, ) values (4, [19,19,19,19,19,19], '404-668-0698', '72 Cascade Point');
-- insert into STORE(store_id, categories, ) values (5, [1], '557-252-8245', '06 Kipling Alley');
-- insert into STORE(store_id, categories, ) values (6, [14,14], '804-936-1553', '7367 Holy Cross Junction');
-- insert into STORE(store_id, categories, ) values (7, [20,20,20,20,20], '470-410-3569', '999 Grasskamp Plaza');
-- insert into STORE(store_id, categories, ) values (8, [9,9,9], '193-792-6040', '00 Morrow Drive');
-- insert into STORE(store_id, categories, ) values (9, [2,2], '898-926-0422', '065 Fremont Plaza');
-- insert into STORE(store_id, categories, ) values (10, [4,4,4], '593-664-3709', '3640 Fieldstone Point');
