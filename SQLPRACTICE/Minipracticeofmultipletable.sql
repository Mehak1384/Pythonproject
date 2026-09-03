create table online_store(
	cx_id  	serial  	primary key,
	cx_name varchar(100) not null,
	city varchar(100) ,
	phone_number integer not null ,
	dob date not null,
	email varchar(100) not null
	
);
create index cx_no on online_store(cx_id);
alter table online_store
alter column phone_number type varchar(20);
insert into online_store(cx_name,city,phone_number,dob,email)
values('Mehak','Mohali','9501589847','2004-08-13','mehakarora1348@gmail.com'),
('Monika','Nodia','9512457893','2003-06-15','monikajanoti18@gmail.com'),
('Promila Devi','MGG','9569149452','1982-01-16','pro123@yahoo.com'),
('Bhavya','Delhi','9915528628','2008-11-4','bhavaya645@gmail.com');
select * from online_store;
create table Products(
product_id serial primary key,
product_name varchar(100) not null, 
category varchar(100) not null, 
price  varchar(100), 
stock varchar(100)
);
create index product_id on Products(product_id);
insert into Products(product_id,product_name, category,price,stock)
values(101,	'Laptop','Electronics','60000','10'),
(102,	'Mouse',	'Electronics','800','50'),
(103,	'Keyboard',	'Electronics','1500','30'),
(104,	'Office Chair','Furniture','5000','15');
create table orders(
order_ID varchar(123), 
cx_id integer not null ,
product_id integer not null,
quantity integer not null, 
order_status varchar(100) not null,
foreign key(cx_id) references online_store(cx_id),
foreign key (product_id) references Products(product_id));
insert into orders(cx_id, product_id, quantity, order_status)
values
(1, 101, 1, 'Delivered'),
(2, 102, 2, 'Delivered'),
(3, 103, 1, 'Pending'),
(4, 104, 2, 'Cancelled'),
(1, 102, 3, 'Delivered');
select*from orders;
alter table orders
drop column order_ID;
select cx_name from online_store;
select cx_name,city,email from online_store;
select*from products;
select product_name,category,price from products;
select*from orders;
select * from online_store where city='Delhi';
select * from online_store where city='Mohali';
alter table products
alter column price type integer
USING price::INTEGER;
select * from products where price>1000;
alter table products 
alter column stock type integer
using stock::integer;
select*from products where stock >20;
select * from orders where order_status='Delivered';
select * from orders where order_status='Pending';
select*from products where category='Electronics';
select*from products where price<5000
select*from products where stock=30
select*from online_store where dob>'2000-1-1';
select*from products where price>=1500;
select * from products where price >1000 and stock >20;
select * from online_store where city='Delhi' or city ='Mohali';
select*from products where category='Electronics' or category='Furniture';
select*from orders where order_status='Delivered'and quantity>1;
select*from online_store where city != 'Delhi';
select distinct city from online_store;
select count(distinct city) from online_store;
select distinct category from products;
select count(distinct category) from products;
select * from products order by price ;
select * from products order by price desc ;
select* from products order by stock desc ;
select*from online_store order by dob;
select*from online_store order by cx_name;



