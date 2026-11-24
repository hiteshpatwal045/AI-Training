show databases;
CREATE DATABASE hitesh_sql_practice;
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10, 2)
);
INSERT INTO employees
VALUES (1, 'Hitesh', 50000.00),
    (2, 'Prince', 60000.00),
    (3, 'Shreyansh', 70000.00),
    (4, 'Pranjali', 55000.00),
    (5, 'Akashdeep', 65000.00),
    (6, 'Shiv', 72000.00),
    (7, 'Rahul', 48000.00),
    (8, 'Anjali', 58000.00),
    (9, 'Nishant', 75000.00),
    (10, 'Kaushik', 68000.00);
select *
from employees;