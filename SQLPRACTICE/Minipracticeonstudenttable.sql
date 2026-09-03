create table student(
		Serial_Number serial not null,
		student_name  varchar(200) not null,
		age     date ,
		gender   Char(10),
		city     Varchar(200),
		course    varchar(100),
		marks     int
);
insert into student(student_name,age,gender,city,course,marks)
values ('Promila Devi','1982-1-16','F','MGG','MA',96),
('Puneet Kumar','1972-12-1','M','Delhi','BA',69),
('Nerru Devi','1983-9-14','F','Tohana','MA',90),
('Dinesh','1974-10-19','M','Tohana','BA',86),
('Dinesh Dora','1982-10-24','M','Tohana','12th',90),
('Sejal Dora','2014-12-17','F','Tohana','7th',100),
('Bhavya','2008-11-04','F','MGG','BE',100),
('Mehak','2004-8-13','F','MGG','MBA',98),
('Ash','1982-1-16','F','MGG','Nursary',100),
('Aniket Sharma','2005-4-24','M','Himachal Pradesh','BCA',46),
('Ruban','2000-12-16','M','Chandigarh','Bcom',89),
('Laxmi Rani','1999-10-16','F','MGG','12th',86),
('Sweety','2020-4-19','F','MGG','Nursary',96),
('Komal rani','1989-1-21','F','Delhi','MA',46),
('Monika Janoti','2003-6-16','F','Nodia','PGDMBA',96);
select * from student;
delete from student where serial_number in (16,17,18,19,20,21,22,23,24,25,26,27,28,29,30);
select * from student;
alter table student 
add column Fees varchar(100);
select*from student; 
update student set Fees ='Unpaid' where course in ('PGDMBA','Nursary','BA','MA');
select*from student;
update student set Fees='Paid'
where course in ('BE','BCA','MBA','12th');
select*from student;
select*from student;
select student_name,course,marks from student ;
select * from student where marks >70;
select * from student where age  between '2000-1-1' and '2006-12-31' ; 
select *from student where city='Delhi' and marks>70;
select * from student where city='Delhi'and city='Chandigarh';
select * from student where city != 'Delhi';
select * from student where course in ('PGDMBA','BA','MA');
select * from student where course not in ('PGDMBA','BA','MA');
select * from student where student_name like 'A%';
select * from student where student_name ilike '%A%';
select * from student where student_name ilike '%n';
update student set city ='Delhi'
where serial_number = 10;
select*from student;
