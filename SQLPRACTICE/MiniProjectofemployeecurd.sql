Drop table if exists employeedata;
create table employeedata(

	Employee_ID 	 Serial not null  Primary key,
	Employee_Name	 text not null ,
	Department       text not null ,
	Salary           int not null ,
	City             varchar(50) not null ,
	Email			 varchar (50) not null 
);
select * from employeedata;
insert into employeedata(Employee_Name,Department,Salary,City,Email)
values('Mehak','Data Engineer',800000,'MGG','mehakarora1348@gmail.com'),
('Bhavya','Navy Officer',900000,'Chandigarh','bhavya234@yahoo.com'),
('Ash','Garud',1000,'MGG','ash@gmail.com'),
('Sejal','Software engineer',500000,'Tohana','Sejal@gmail.com'),
('Promila Devi','Hindi Teacher',4000000,'Khanna','promila@samsung.com');
select * from employeedata;
select employee_name from employeedata;
select * from employeedata
where department='Hindi Teacher';
select * from employeedata
where salary >500000;
select * from employeedata
where city='delhi';
update employeedata
set department='IT department'
where department ='Data Engineer'; 
select * from employeedata
update employeedata
set city='Mumbai'
where employee_name='Mehak';
select * from employeedata
where employee_name='Mehak'
update employeedata
set salary=salary+salary*0.1
select * from employeedata;
Alter table employeedata
drop column if exists phone_number;
Alter table employeedata
add phone_number int;
select * from employeedata;
insert into employeedata(Employee_Name,Department,Salary,City,Email,phone_number)
values('Mehak','Data Engineer',800000,'MGG','mehakarora1348@gmail.com',1348),
('Bhavya','Navy Officer',900000,'Chandigarh','bhavya234@yahoo.com',4567),
('Ash','Garud',1000,'MGG','ash@gmail.com',4555),
('Sejal','Software engineer',500000,'Tohana','Sejal@gmail.com',44),
('Promila Devi','Hindi Teacher',4000000,'Khanna','promila@samsung.com',4455);
select*from employeedata;
delete from employeedata
where Employee_ID  =7;
delete from employeedata
where Employee_ID  =8;
delete from employeedata
where Employee_ID  =9;
delete from employeedata
where Employee_ID  =10;
delete from employeedata
where Employee_ID  =11;
select*from employeedata;
update employeedata
set phone_number=4567
where employee_id=1;
update employeedata
set phone_number=4507
where employee_id=2;
update employeedata
set phone_number=4557
where employee_id=3;
update employeedata
set phone_number=8567
where employee_id=4;
update employeedata
set phone_number=45673
where employee_id=5;
select*from employeedata;
alter table employeedata
alter column employee_name type varchar(200);
alter table employeedata
alter column department set not null;
alter table employeedata
alter column city set default 'delhi';
select*from employeedata;
alter table employeedata
drop column if exists phone_number;
select*from employeedata;
delete from employeedata
where department='Garud';
delete from employeedata
where employee_id=2;
delete from employeedata
where salary>1000000 or salary<50000;
select * from employeedata;




