compute_hours = int(input("Enter compute hours: "))
storage = int(input("Enter storage used (GB): "))
plan = input("Enter plan (Basic/Premium/Enterprise): ")

if plan == "Basic":
    bill = (compute_hours * 10) + (storage * 2) + 500
elif plan == "Premium":
    bill = (compute_hours * 8) + (storage * 2) + 1500
elif plan == "Enterprise":
    bill = (compute_hours * 5) + (storage * 1.5) + 5000
else:
    print("Invalid plan")
    exit()
    
print("Final Bill =", bill)