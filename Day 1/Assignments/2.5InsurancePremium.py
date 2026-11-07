age = int(input("Enter age: "))
smoking = input("Smoking habit (Yes/No): ")
bmi = float(input("Enter BMI: "))
disease = input("Pre-existing disease (Y/N): ")

if age > 50:
    print("High Premium")
elif bmi >= 25 and bmi <= 29.9:
    print("Medium Premium")
elif age > 60 and disease == "Y":
    print("Reject")
elif disease == "N" and age <= 50:
    print("Low Premium")
