#Step 1 Import Numpy
import numpy as np

#step 2 Create salary Array
salary = np.array([65000,58000,72000,80000,85000,68000,90000,76000])
print("-------------salary----------")
print(salary)

#step 3 Cehck Numpy Array Properties
print("--------------Salary Operations------------")
print("Array ", salary)
print("Type", type(salary))
print("Dimensions ", salary.ndim)
print("Shape ", salary.shape)
print("Size ", salary.size)
print("Data Type ", salary.dtype)

salary1 = np.array([[[65000,58000,72000,80000,85000,68000,90000,76000]]])
print("Shape ", salary1.shape)
print("Dimensions ", salary1.ndim)


rating = np.array([4,5,4,2,4,8,4,6])
print("====================Ratings===============")
print(rating)

#Check properties
print("=============Ratings Properties============")
print("Rating Shape: ", rating.shape)
print("Rating size: ", rating.size)
print("Rating Data Type: ", rating.dtype)

#Step 5 - numpy Indexing
print("==============Numpy Indexing=============")
print("First Salary : ", salary[0])
print("Third Salary : ", salary[2])
print("Last Salary : ", salary[-1])
print("Second Last Salary : ", salary[-2])
print("Third Last Salary : ", salary[-3])

#salary = np.array([65000,58000,72000,80000,85000,68000,90000,76000])

#Step 6 - Numpy Slicing
#First three:
print("==============Numpy Slicing==============")
print("First 3 Salary : ", salary[0:3])

#Last Three:
print(salary[-3:])

#All except first two:
print(salary[2:])

#Find Employees Earning Above 75000
#Business: Identify employees in a higher salary bracket.
print("=========== Salary Above 75000 ============")

high_salary = salary[salary > 75000]
print("Emp salary : ", high_salary)
print("Salary Count : ", len(high_salary))

print("==============High Performing Employees=============")

high_rating = rating[rating  > 4.5]

print("Hight Rating: ", high_rating)
print("Num of Emp: ", len(high_rating))


#Conditional Salary Increment
#Business : Employee earning below 70000 get 10% increment.
#other employees receive 5%

new_salary = np.where(salary < 70000, salary * 1.10, salary * 1.05)
print("Original salary : ", salary)
print("Updated salary : ", new_salary)

#Performance-Based Bonus
#Business: Employees rated 4.5 or above receive 15% bonus.
#Other employees receive 5%.
print("============Performance Bonus==============")

bonus = np.where(
    rating >= 4.5,
    salary * 0.15,
    salary * 0.05
)
print("Employee Bonus: ", bonus)

#Calculate Salary After Bonus
#Business: Calculate salary plus performance bonus.

print("===============Salary After Bonus================")
salary_with_bonus = salary + bonus

print("Original Salary: ", salary)
print("Bonus: ", bonus)
print("Salary After Bonus: ", salary_with_bonus)

#Find Salary Standard Deviation 
#Business: Measure variation in employee salaries.
salary_std = np.std(salary)
print("Standard Deviation: ", salary_std)
