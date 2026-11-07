amount = int(input("Enter the purchase amount : "))

if amount >= 5000:
    amount += (.2 * amount)
elif amount >= 30000 and amount < 50000:
    amount += (10 / 100 * amount)
else:
    amount += (5 / 100 * amount)

print(f"The purchase amount after discount is {amount}")
