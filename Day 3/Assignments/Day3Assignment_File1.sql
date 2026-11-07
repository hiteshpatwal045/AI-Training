CREATE DATABASE IF NOT EXISTS hsbc_bank; 

USE hsbc_bank; 
 
CREATE TABLE Departments ( 

 department_id INT PRIMARY KEY, 

 department_name VARCHAR(80) NOT NULL UNIQUE, 

 location VARCHAR(60) NOT NULL, 

 annual_budget DECIMAL(14,2) NOT NULL 

); 

 

CREATE TABLE Employees ( 

 employee_id INT PRIMARY KEY, 

 first_name VARCHAR(50) NOT NULL, 

 last_name VARCHAR(50) NOT NULL, 

 email VARCHAR(120) NOT NULL UNIQUE, 

 gender VARCHAR(20), 

 hire_date DATE NOT NULL, 

 designation VARCHAR(80) NOT NULL, 

 department_id INT NOT NULL, 

 manager_id INT NULL, 

 base_salary DECIMAL(12,2) NOT NULL, 

 employment_status VARCHAR(20) NOT NULL, 

 FOREIGN KEY (department_id) REFERENCES Departments(department_id), 

 FOREIGN KEY (manager_id) REFERENCES Employees(employee_id) 

); 

 

CREATE TABLE Payroll ( 

 payroll_id INT PRIMARY KEY, 

 employee_id INT NOT NULL, 

 pay_month DATE NOT NULL, 

 basic_pay DECIMAL(12,2) NOT NULL, 

 bonus DECIMAL(12,2) NOT NULL DEFAULT 0, 

 allowances DECIMAL(12,2) NOT NULL DEFAULT 0, 

 deductions DECIMAL(12,2) NOT NULL DEFAULT 0, 

 net_pay DECIMAL(12,2) GENERATED ALWAYS AS 

   (basic_pay + bonus + allowances - deductions) STORED, 

 payment_status VARCHAR(20) NOT NULL, 

 UNIQUE (employee_id, pay_month), 

 FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) 

); 

 

CREATE TABLE Projects ( 

 project_id INT PRIMARY KEY, 

 project_name VARCHAR(100) NOT NULL, 

 project_type VARCHAR(60) NOT NULL, 

 start_date DATE NOT NULL, 

 end_date DATE NULL, 

 budget DECIMAL(14,2) NOT NULL, 

 project_status VARCHAR(25) NOT NULL 

); 

 

CREATE TABLE EmployeeProjects ( 

 assignment_id INT PRIMARY KEY, 

 employee_id INT NOT NULL, 

 project_id INT NOT NULL, 

 assigned_date DATE NOT NULL, 

 role_on_project VARCHAR(60) NOT NULL, 

 allocation_pct INT NOT NULL, 

 UNIQUE (employee_id, project_id), 

 CHECK (allocation_pct BETWEEN 1 AND 100), 

 FOREIGN KEY (employee_id) REFERENCES Employees(employee_id), 

 FOREIGN KEY (project_id) REFERENCES Projects(project_id) 

); 