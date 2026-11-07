salary = int(input("Enter the salary: "))

if salary >= 50000:
    salary += (20 / 100 * salary)
elif salary >= 30000 and salary < 50000:
    salary += (10 / 100 * salary)
else:
    salary += (5 / 100 * salary)

print(f"The salary after bouns is {salary}")