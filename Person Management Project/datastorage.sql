create table student_management(
		student_id 		serial			 not null 		Primary key,
		first_name 		varchar(100)     not null ,
		last_name       varchar(100)     not null,
		is_male         boolean ,
		dob             date			 not null,
		email			varchar(100)    not null       unique,
		phone           varchar(20)     unique,
		course           varchar(20)    not null,
		city             varchar(50)    not null);
CREATE INDEX student_management_idx_name
ON student_management(first_name,last_name);
Insert into student_management(first_name,last_name,is_male,dob,email,phone,course,city)
values('Mehak','Arora',False,'2004-08-13','mehakarora1348@gmail.com','950158987','BCA','MGG'),
('Bhavya','Arora',False,'2008-11-04','bhavyaarora649@gamil.com','9915528679','Btech','MGG'),
('Sejal','Dora',False,'2014-12-17','sejal123@yahoo.com','9876542210','BCA','Tohana'),
('Jeeval','Demla',False,'2011-01-07','jeeval12@gmail.com','9876534120','Diploma','Pataila'),
('Gunav','N/A',True,'2013-12-08','gunav@gmail.com','9090897889','Btech','Pataila');
select*from student_management;
select *from student_management where student_id=1 or last_name='Arora';
select*from student_management where course='BCA'and city ='Tohana';
update student_management
set first_name='Ash',
last_name='Arora',
email='ashu@gmail.com',
phone='9569149452',
Course='schooling',
dob='2020-5-22'
where student_id=4;
select*from student_management;
delete from student_management where student_id=5;
select*from student_management;
delete from student_management where course='schooling';
select*from student_management;
delete from student_management where student_id=2;
Insert into student_management(first_name,last_name,is_male,dob,email,phone,course,city)
values ('Jeeval','Demla',False,'2011-01-07','jeeval12@gmail.com','9876534120','Diploma','Pataila'),
('Gunav','N/A',True,'2013-12-08','gunav@gmail.com','9090897889','Btech','Pataila');
select*from student_management;
select *from student_management where course='BCA';
select*from student_management where city='Pataila';
select*from student_management where student_id>2;
select*from student_management where student_id<=3;
select*from student_management where last_name<>'Arora';
select*from student_management where last_name!='N/A';
select*from student_management where course='BCA'and city='MGG';
select*from student_management where city='Delhi' or city='Tohana';
select*from student_management where course<>'Btech';
select*from student_management where dob between '2008-01-01' and '2015-12-31';
select*from student_management where student_id between '0' and '3';
select*from student_management where city in ('MGG','Tohana');
select*from student_management where course in ('BCA','Diploma');
select*from student_management where first_name ilike 'M%';
select*from student_management where first_name ilike '%l';
select*from student_management where email like '%gmail.com';
select*from student_management where city like'P%';
select*from student_management where phone=Null;
select*from student_management where phone is Not Null;
select*from student_management where is_male=false and city='MGG' and course='BCA';
select*from student_management where city in ('Pataila','Tohana') and course<>'Diploma';
select*from student_management where first_name Ilike 'A%' or first_name ilike 'M%';
select *from student_management where student_id not between '2' and '4';
select*from student_management where email not ilike '%gmail.com';
select*from student_management where is_male = true;









		
		
		
