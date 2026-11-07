show databases;

CREATE database Coforge_db;

use Coforge_db;

create table Employee(
EmpId int primary key auto_increment,
EmpName varchar(20),
EmpAge int,
EmpEmail varchar(50),
EmpSalary decimal(10,2),
EmpCity varchar(50)
);

select* from employee;

INSERT INTO Employee (EmpName, EmpAge, EmpEmail, EmpSalary, EmpCity) VALUES
('Shiv',23,'shiv1@gmail.com',45000,'Pune'),
('Atharva',22,'atharva1@gmail.com',42000,'Mumbai'),
('Pranjali',24,'pranjali1@gmail.com',48000,'Nagpur'),
('Akash',25,'akash1@gmail.com',50000,'Delhi'),
('Hitesh',23,'hitesh1@gmail.com',46000,'Pune'),
('Sahil',22,'sahil1@gmail.com',41000,'Mumbai'),
('Shreyansh',24,'shreyansh1@gmail.com',47000,'Hyderabad'),
('Prince',26,'prince1@gmail.com',55000,'Indore'),
('Rohit',27,'rohit1@gmail.com',52000,'Pune'),
('Aman',25,'aman1@gmail.com',49000,'Delhi'),
 
('Neha',24,'neha1@gmail.com',45000,'Mumbai'),
('Pooja',23,'pooja1@gmail.com',43000,'Pune'),
('Kunal',28,'kunal1@gmail.com',60000,'Bengaluru'),
('Vikas',29,'vikas1@gmail.com',62000,'Chennai'),
('Anjali',22,'anjali1@gmail.com',40000,'Nagpur'),
('Sneha',24,'sneha1@gmail.com',47000,'Pune'),
('Nikhil',26,'nikhil1@gmail.com',53000,'Hyderabad'),
('Harsh',27,'harsh1@gmail.com',58000,'Mumbai'),
('Tushar',25,'tushar1@gmail.com',51000,'Delhi'),
('Deepak',30,'deepak1@gmail.com',70000,'Bengaluru'),
 
('Shivam',24,'shivam1@gmail.com',45000,'Pune'),
('Atharva2',23,'atharva2@gmail.com',42000,'Mumbai'),
('Pranjal',25,'pranjal1@gmail.com',48000,'Nagpur'),
('Akshay',26,'akshay1@gmail.com',50000,'Delhi'),
('Hitesh2',24,'hitesh2@gmail.com',46000,'Pune'),
('Sahil2',23,'sahil2@gmail.com',41000,'Mumbai'),
('Shrey',25,'shrey1@gmail.com',47000,'Hyderabad'),
('Prince2',27,'prince2@gmail.com',55000,'Indore'),
('Rohit2',28,'rohit2@gmail.com',52000,'Pune'),
('Aman2',26,'aman2@gmail.com',49000,'Delhi'),
 
('Neha2',25,'neha2@gmail.com',45000,'Mumbai'),
('Pooja2',24,'pooja2@gmail.com',43000,'Pune'),
('Kunal2',29,'kunal2@gmail.com',60000,'Bengaluru'),
('Vikas2',30,'vikas2@gmail.com',62000,'Chennai'),
('Anjali2',23,'anjali2@gmail.com',40000,'Nagpur'),
('Sneha2',25,'sneha2@gmail.com',47000,'Pune'),
('Nikhil2',27,'nikhil2@gmail.com',53000,'Hyderabad'),
('Harsh2',28,'harsh2@gmail.com',58000,'Mumbai'),
('Tushar2',26,'tushar2@gmail.com',51000,'Delhi'),
('Deepak2',31,'deepak2@gmail.com',70000,'Bengaluru');


select * from Employee;

select * from Employee where EmpSalary>50000;

select * from Employee where EmpAge<25;

select * from Employee where EmpSalary=45000;

select * from Employee where EmpCity<>'pune';

select * from Employee where EmpSalary between 40000 AND 45000;

select * from Employee where EmpCity in('pune','delhi');

select * from Employee where EmpAge between 25 And 27;

select * from Employee where EmpCity='pune' And EmpSalary>45000;

select * from Employee where EmpName Like '%sh%';

select * from Employee order by Empsalary DESC;


select * from Employee order by EmpSalary DESC LIMIT 5;

select * from Employee order by EmpCity, EmpSalary DESC;

select COUNT(*) as 'Total Employee' from Employee;

select MIN(EmpSalary) as 'Minimum Salary' from Employee;


select MAX(EmpSalary) as 'Maximum Salary' from Employee;

select ROUND(AVG(Empsalary),2) as 'Average Salary' from Employee;

select SUM(EmpSalary) as 'Employee Expenditure' from Employee;

select COUNT(EmpSalary) as 'Greater than 50k' from Employee where EmpSalary>50000;

select MAX(EmpSalary)-MIN(EmpSalary) from Employee;

select EmpCity, COUNT(EmpCity) as 'count city' from Employee group by EmpCity, EmpName;

-- calculate each city -salary, min, and max, and total expenditure in each city;

select EmpCity, MIN(EmpSalary), Max(EmpSalary), SUM(EmpSalary) as 'Total Expenditure', COUNT(EmpCity) as 'count city' from Employee group by EmpCity, EmpName;

select EmpCity, COUNT(EmpID) as 'Employee Count' from Employee group by EmpCity having Count(EmpCity)>4;

select EmpCity, AVG(EmpSalary) as 'Average Salary' from Employee group by EmpCity having AVG(EmpSalary)>50000;

select EmpAge, COUNT(EmpID) as 'Total Employee' from Employee group by EmpAge having COUNT(EmpAge)>3;
