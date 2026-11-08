-- Q001. List all databases on the server. 
show databases;

-- Q002. Select the hsbc_bank database. 
use hsbc_bank;

-- Q003. List all tables in hsbc_bank. 
show tables;

-- Q004. Describe the structure of Employees. 
describe employees;

-- Q005. Describe the structure of Payroll. 
describe Payroll;

-- Q006. Display every column of Employees. 
SELECT * FROM employees;

-- Q007. Display employee_id, first_name and last_name only. 
SELECT employee_id, first_name, last_name FROM employees;

-- Q008. Display distinct designations. 
SELECT DISTINCT designation FROM employees;

-- Q009. Display distinct department locations. 
select distinct location from departments;

-- Q010. Retrieve all department names and annual budgets. 
SELECT department_name, annual_budget FROM Departments;

-- Q011. Retrieve the first 10 employees ordered by employee_id.
select * from Employees order by employee_id LIMIT 10;

-- Q012. Create a full_name alias by concatenating first_name and last_name. 
select concat(first_name, ' ', last_name) as Full_Name from Employees;

-- Q013. Show employee name and annualized base salary (base_salary * 12). 
select concat(first_name, ' ', last_name) as employee_name, (base_salary * 12) as annual_salary from Employees;

-- Q014. Display all project names, statuses and budgets. 
SELECT project_name, project_status, budget FROM Projects;

-- Q015. List payroll records with calculated net_pay. 
SELECT payroll_id, employee_id, pay_month, net_pay FROM Payroll;

-- Q016. Find employees with base_salary greater than 90000. 
SELECT * FROM Employees 
WHERE base_salary > 90000;

-- Q017. Find employees earning between 60000 and 110000. 
SELECT * FROM Employees 
WHERE base_salary BETWEEN 60000 AND 110000;

-- Q018. Find employees hired on or after 2024-01-01. 
select * from Employees 
where hire_date >= '2024-01-01';

-- Q019. List active employees only. 
SELECT * FROM Employees 
WHERE employment_status = 'Active';

-- Q020. Find employees whose first name begins with A. 
SELECT * FROM Employees 
WHERE first_name Like 'A%';

-- Q021. Find employees whose last name contains a. 
SELECT * FROM Employees 
WHERE last_name LIKE '%a%';

-- Q022. Find employees in department IDs 1, 3 or 5. 
select * from employees
where department_id IN (1,3,5);

-- Q023. Find employees with no manager assigned. 
SELECT * FROM Employees 
WHERE manager_id IS NULL;

-- Q024. List employees sorted by salary highest first. 
select * from Employees 
order by base_salary desc;

-- Q025. Show the five highest-paid employees. 
SELECT * FROM Employees 
ORDER BY base_salary DESC 
LIMIT 5;

-- Q026. List projects with a NULL end_date. 
SELECT * FROM Projects 
WHERE end_date IS NULL;

-- Q027. Find projects with budgets above 7000000. 
SELECT * FROM Projects 
WHERE end_date IS NULL;

-- Q028. Find payroll records whose payment_status is Pending. 
SELECT * FROM Payroll 
WHERE payment_status = 'Pending';

-- Q029. List employees hired during calendar year 2025 using a date range. 
SELECT * FROM Employees 
WHERE hire_date BETWEEN '2025-01-01' AND '2025-12-31';

-- Q030. Display employee names in uppercase. 
SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS employee_name_uppercase FROM Employees;

-- Q031. Show the length of each employee first name. 
SELECT first_name, LENGTH(first_name) AS name_length FROM Employees;

-- Q032. Show each employee hire year using YEAR(). 
SELECT employee_id, first_name, last_name, YEAR(hire_date) AS hire_year FROM Employees;

-- Q033. Display salaries rounded to the nearest thousand. 
SELECT employee_id, first_name, last_name, ROUND(base_salary, -3) AS rounded_salary FROM Employees;

-- Q034. Show employees whose designation is Analyst or Associate. 
SELECT * FROM Employees 
WHERE designation IN ('Analyst', 'Associate');

-- Q035. Show active employees ordered by department and salary descending.
SELECT * FROM Employees 
WHERE employment_status = 'Active' 
ORDER BY department_id ASC, base_salary DESC;

-- Q040. Count employees in each department_id. 
SELECT department_id, COUNT(*) AS employee_count 
FROM Employees 
GROUP BY department_id;

-- Q041. Find average base salary by department_id. 
SELECT department_id, AVG(base_salary) AS avg_salary 
FROM Employees 
GROUP BY department_id;

-- Q042. Find highest base salary in each department_id. 
SELECT department_id, MAX(base_salary) AS max_salary 
FROM Employees 
GROUP BY department_id;

-- Q043. Find departments with more than four employees using HAVING. 
SELECT department_id, COUNT(*) AS employee_count 
FROM Employees 
GROUP BY department_id 
HAVING COUNT(*) > 4;

-- Q044. Find departments whose average salary exceeds 80000. 
SELECT department_id, AVG(base_salary) AS avg_salary 
FROM Employees 
GROUP BY department_id 
HAVING AVG(base_salary) > 80000;

-- Q045. Count employees by designation. 
SELECT designation, COUNT(*) AS employee_count 
FROM Employees 
GROUP BY designation;

-- Q046. Find designations with at least three employees. 
SELECT designation, COUNT(*) AS employee_count 
FROM Employees 
GROUP BY designation 
HAVING COUNT(*) >= 3;

-- Q047. Calculate total net payroll for each pay_month. 
SELECT pay_month, SUM(net_pay) AS total_net_payroll 
FROM Payroll 
GROUP BY pay_month;

-- Q048. Calculate total bonus paid for each pay_month. 
SELECT pay_month, SUM(bonus) AS total_bonus_paid 
FROM Payroll 
GROUP BY pay_month;

-- Q049. Find payroll months with total deductions above 200000. 
SELECT pay_month, SUM(deductions) AS total_deductions 
FROM Payroll 
GROUP BY pay_month 
HAVING SUM(deductions) > 200000;

-- Q050. Count Paid versus Pending payroll rows by month. 
SELECT pay_month, payment_status, COUNT(*) AS row_count 
FROM Payroll 
GROUP BY pay_month, payment_status;

-- Q051. Find the average budget of Active projects. 
SELECT AVG(budget) AS avg_active_project_budget 
FROM Projects 
WHERE project_status = 'Active';

-- Q052. Count projects by project_status. 
SELECT project_status, COUNT(*) AS project_count 
FROM Projects 
GROUP BY project_status;

-- Q053. Find project statuses with more than one project. 
SELECT project_status, COUNT(*) AS project_count 
FROM Projects 
GROUP BY project_status 
HAVING COUNT(*) > 1;

-- Q054. Calculate total project budget by project_type. 
SELECT project_type, SUM(budget) AS total_budget 
FROM Projects 
GROUP BY project_type;

-- Q055. Find departments where the maximum employee salary exceeds 120000. 
SELECT department_id, MAX(base_salary) AS max_salary 
FROM Employees 
GROUP BY department_id 
HAVING MAX(base_salary) > 120000;

-- Q056. INNER JOIN Employees and Departments to show employee full name and department name. 
select concat(e.first_name, ' ', e.last_name) as full_name, d.department_name 
from employees e
INNER join Departments d ON e.department_id = d.department_id;

-- Q057. Show employee name, designation and department location using a two-table join. 
select concat(e.first_name, ' ', e.last_name) as employee_name, e.designation, d.location
from employees e
INNER JOIN departments d on e.department_id = d.department_id;

-- Q058. List all employees in the Technology department using a join. 
select e.* 
from employees e 
Inner join departments d ON e.department_id = d.department_id
where d.department_name = 'Technology';

-- Q059. Show employee name, department name and base salary, ordered by salary. 
SELECT CONCAT(e.first_name, ' ', e.last_name) AS employee_name, d.department_name, e.base_salary
from employees e
Inner Join Departments d on e.department_id = d.department_id
order by e.base_salary desc;

-- Q060. Count employees per department using Employees JOIN Departments. 
select d.department_name, count(e.employee_id) as employee_count
from departments d
left join employees e on d.department_id = e.department_id
group by d.department_name;

-- Q061. Show department name and average employee salary using JOIN and GROUP BY. 
SELECT d.department_name, AVG(e.base_salary) AS average_salary 
FROM Departments d
INNER JOIN Employees e ON d.department_id = e.department_id
GROUP BY d.department_name;

-- Q062. Find department names with at least five employees using JOIN, GROUP BY and HAVING. 
select d.department_name, count(e.employee_id) as employee_count
from departments d
inner join employees e on d.department_id = e.department_id
group by d.department_name
having count(e.employee_id) >= 5;

-- Q063. JOIN Employees and Payroll to show employee name, pay_month and net_pay. 
select concat(e.first_name, ' ', e.last_name) as emp_name, p.pay_month, p.net_pay
from Employees e
inner join payroll p on e.employee_id = p.employee_id;

-- Q064. Find employees whose October 2026 payroll is Pending using two tables. 
select concat(e.first_name, ' ', e.last_name) as emp_name
from employees e
inner join payroll p on e.employee_id = p.employee_id
where p.pay_month = '2026-10-01' and  p.payment_status = 'Pending';

-- Q065. Show employee names and bonuses for September 2026. 
select concat(e.first_name, ' ', e.last_name) as emp_name, p.bonus
from employees e
inner join payroll p on e.employee_id = p.employee_id
where p.pay_month = '2026-09-01';

-- Q066. Find total net_pay for each employee across three months using Employees and Payroll. 



-- Q067. Show the five employees with the highest total net_pay across all months. 


-- Q068. JOIN EmployeeProjects and Projects to show project names and assignment roles. 


-- Q069. JOIN Employees and EmployeeProjects to list employees and their allocation percentages. 


-- Q070. Count assigned employees per project using Projects and EmployeeProjects. 


-- Q071. Use LEFT JOIN to list every project, including projects with no assignments. 


-- Q072. Use LEFT JOIN to find employees who have no project assignments. 


-- Q073. Use a self JOIN on Employees to show each employee and their manager name. 


-- Q074. Use LEFT self JOIN to include managers who have no manager_id. 


-- Q075. Show employees whose manager earns less than they do using a self JOIN.











-- Q076. Join Employees, Departments and Payroll to show employee, department, month and net pay. 


-- Q077. Find total net payroll by department for October 2026 using three tables. 


-- Q078. Find departments with October 2026 total net payroll greater than 500000. 


-- Q079. Join Employees, EmployeeProjects and Projects to list each employee with project name and role. 


-- Q080. Find all Active projects and the names of employees assigned to them. 


-- Q081. Show the number of distinct projects per employee using a three-table join. 


-- Q082. Find employees assigned to two or more projects using GROUP BY and HAVING. 


-- Q083. Show department names and number of distinct projects worked on by their employees. 


-- Q084. Find the highest-paid employee in each department using a correlated subquery. 


-- Q085. Find employees whose base_salary is above the overall average salary. 


-- Q086. Find employees earning more than their own department average using a correlated subquery. 


-- Q087. Find projects with budgets above the average project budget. 


-- Q088. Find employees who have never received a bonus using NOT EXISTS. 


-- Q089. Find employees who have at least one Pending payroll record using EXISTS. 


-- Q090. Find employees assigned to projects whose budget exceeds 8000000 using IN or EXISTS. 


-- Q091. Use CASE to classify salaries as High (>= 100000), Medium (>= 70000) or Low. 


-- Q092. Use CASE to categorize project budgets as Large (>= 8000000) or Standard. 


-- Q093. Use a CTE to calculate total net_pay per employee and return the top ten. 


-- Q094. Use a CTE to calculate departmental average salary and return above-average departments. 


-- Q095. Build a final dashboard query showing each department, employee count, average base salary, and October 2026 total net payroll; include departments with no employees. 


-- Q096. Find the project with the greatest number of assigned employees. 


-- Q097. Find employees whose total project allocation exceeds 100 percent. 


-- Q098. Compare each employee October net pay against the department October average using a CTE. 


-- Q099. Find departments with no employees assigned to any Active project using NOT EXISTS. 


-- Q100. Rank employees by base salary within each department using DENSE_RANK(). 

