CREATE DATABASE EmployeeDB;
USE EmployeeDB;
CREATE TABLE Employees (
   employee_id INT AUTO_INCREMENT PRIMARY KEY,
   employee_name VARCHAR(100) NOT NULL,
   age INT NOT NULL,
   email VARCHAR(150) NOT NULL UNIQUE,
   department VARCHAR(100) NOT NULL,
   designation VARCHAR(100) NOT NULL,
   salary DECIMAL(12,2) NOT NULL,
   city VARCHAR(100) NOT NULL
);

INSERT INTO Employees
(employee_name, age, email, department,
designation, salary, city)
VALUES
('Amit Sharma', 28, 'amit@gmail.com',
'IT', 'Developer', 65000, 'Pune'),
('Priya Verma', 30, 'priya@gmail.com',
'HR', 'HR Manager', 75000, 'Mumbai'),
('Rahul Singh', 26, 'rahul@gmail.com',
'IT', 'Python Developer', 55000, 'Delhi'),
('Neha Gupta', 32, 'neha@gmail.com',
'Finance', 'Analyst', 80000, 'Pune'),
('Rohit Mehta', 29, 'rohit@gmail.com',
'IT', 'Team Lead', 95000, 'Bengaluru');
select * from Employees