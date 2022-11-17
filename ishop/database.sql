select * from auth_user;
select * from auth_user_groups;
select * from sqlite_schema;
select * from django_session;


drop table store_cartitem;
drop table store_orderdetail;
drop table store_order;
drop table store_customer;
drop table store_cart;
drop table store_shippingaddress;
drop table store_payment;
drop table store_product;
drop table store_inventory;
drop table store_category;




create table "store_customer" ("id" integer not null primary key autoincrement, first_name varchar(100) not null, last_name varchar(100) not null, phone varchar(100), email varchar(100), user_id integer references "auth_user"(id), cart_id integer references "store_cart"(id));
create table "store_cart" ("id" integer not null primary key autoincrement, session_id varchar(100) not null);
create table "store_shippingaddress" ("id" integer not null primary key autoincrement, street varchar(100) not null, city varchar(100) not null, zipcode integer not null, country varchar(100));
create table "store_payment" ("id" integer not null primary key autoincrement, amount integer not null default 0, status integer not null default 0);
create table "store_order" ("id" integer not null primary key autoincrement, amount integer not null default 0, shipping_address_id integer not null references "store_shipping_address"(id), customer_id integer not null references "store_customer"(id), payment_id integer not null references "store_payment"(id));
create table "store_category" ("id" integer not null primary key autoincrement, ref_id integer references "store_category"(id), name varchar(100) not null);
create table "store_inventory" ("id" integer not null primary key autoincrement, quantity integer not null default 0);
create table "store_product" ("id" integer not null primary key autoincrement, name varchar(100) not null, price integer not null, description varchar(100), image1_url varchar(255), image2_url varchar(255), image3_url varchar(255), image4_url varchar(255), category_id integer not null references "store_category"(id), inventory_id integer not null references "store_inventory"(id));
create table "store_cartitem" ("id" integer not null primary key autoincrement, quantity integer not null default 0, product_id integer not null references "store_product"(id), cart_id integer not null references "store_cart"(id));
create table "store_orderdetail" ("id" integer not null primary key autoincrement, quantity integer not null default 0, product_id integer not null references "store_product"(id), order_id integer not null references "store_order"(id));



pragma foreign_keys=off;

--begin transaction;

alter table store_orderdetail rename to _store_orderdetail_old;
create table "store_orderdetail" ("id" integer not null primary key autoincrement, quantity integer not null, product_id integer not null references "store_product"(id), order_id integer not null references "store_order"(id));

insert into store_orderdetail select * from _store_orderdetail_old;

drop table _store_orderdetail_old;

--commit;

pragma foreign_keys=on;



select * from store_cart;
select * from store_customer;
select * from store_shippingaddress;
select * from store_payment;
select * from store_order;
select * from store_category;
select * from store_inventory;
select * from store_product;
select * from store_cartitem;
select * from store_orderdetail;


insert into store_cart ("session_id") values ("a67nj44ci8hy7o6r70gwybijwkyzevqb");
insert into store_customer ("first_name","last_name","phone","email",user_id,cart_id) values ('john', 'doe','', 'john.doe@email.com', null, 1);
insert into store_shippingaddress ("street", "city", "zipcode", "country") values ('Kungsgatan 1', 'Stockholm', 11135, 'Sweden');
insert into store_payment ("amount","status") values (123,0);
insert into store_order ("amount", "shipping_address_id", "customer_id", "payment_id") values (123, 1, 1, 1);
insert into store_category ("ref_id", "name") values (null, 'Computers');
insert into store_category ("ref_id", "name") values (1, 'Laptop');
insert into store_category ("ref_id", "name") values (1, 'Desktop');
insert into store_category ("ref_id", "name") values (null, 'Network');
insert into store_category ("ref_id", "name") values (4, 'Routers');
insert into store_inventory ("quantity") values (10);
insert into store_inventory ("quantity") values (20);
insert into store_product ("name", "price", "description", "image1_url", "image2_url", "image3_url", "image4_url", "category_id", "inventory_id") values ('Lenovo', 12345, 'A Lenovo Laptop', '/media/lenovo1.jpg', '/media/lenovo2.jpg', '/media/lenovo3.jpg', '/media/lenovo4.jpg', 2, 1);
insert into store_product ("name", "price", "description", "image1_url", "image2_url", "image3_url", "image4_url", "category_id", "inventory_id") values ('Acer', 12346, 'An Acer Laptop', '/media/acer1.jpg', '/media/acer2.jpg', '/media/acer3.jpg', '/media/acer4.jpg', 2, 2);
insert into store_cartitem ("quantity", "product_id", "cart_id") values (1, 1, 1);
insert into store_orderdetail ("quantity", "product_id", "order_id") values (3, 2, 1);


--check product list
select * from store_product p
inner join store_category c
on p.category_id = c.id
inner join store_inventory i
on p.inventory_id = i.id
where c.ref_id = 1


--check order
select o.amount, p.name, p.price, p.description, od.quantity, 
od.order_id, c.first_name, c.last_name, sa.street, sa.city, sa.zipcode, sa.country
from store_order o
inner join store_orderdetail od on
o.id = od.order_id
inner join store_product p on
od.product_id = p.id
inner join store_customer c on
c.id = o.customer_id
inner join store_shippingaddress sa on
sa.id = o.shipping_address_id;


--check cart content
select * from store_cart c
inner join store_cartitem ci
on c.id = ci.cart_id
inner join store_product p
on p.id = ci.product_id