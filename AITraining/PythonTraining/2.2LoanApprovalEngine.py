monthlySalary = float(input("enter salary: "))
creditScore = float(input("enter credit Score: "))
loanAmount = float(input("Enter existing Loan Amount: "))
empType = input("enter employmnet Type: ")

req = ""

if monthlySalary > 80000 and creditScore > 750 and loanAmount < 20000:
    req = "approved"
elif monthlySalary > 50000 and creditScore > 650:
    req = "Approved with Caution"
elif creditScore < 600:
    req = "Rejected"
else:
    req = "manual review"

print(f"for the current input the load req is : {req}")

