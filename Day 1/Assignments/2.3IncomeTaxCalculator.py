income = float(input("enter annual income"))
age = int(input("Enter age"))
amount = int(input("Enter investment amount"))

tax = 0

if age >= 60:
    print("allow senior citizen exemption")
elif income < 500000:
    print(f"tax for income < 500000 is : {tax}")
elif income >= 500000 and income < 1000000:
    print(f"tax for income between 500000 and 1000000 is :{tax * .1}")
elif income >= 1000000 and income < 2000000:
    print(f"tax for income between 1000000 and 2000000 is :{tax * .2}")
else:
    print(f"tax above 2000000 is : {tax * .3}") 
