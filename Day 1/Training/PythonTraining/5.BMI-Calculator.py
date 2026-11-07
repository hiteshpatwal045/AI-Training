weight = float(input("Enter the Weight : "))
height = float(input("Enter the Height : "))

bmi = weight / (height*height)

if bmi >= 30:
    print("Obese")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
else:
    print("UnderWeight")

print(f"BMI is {bmi}")