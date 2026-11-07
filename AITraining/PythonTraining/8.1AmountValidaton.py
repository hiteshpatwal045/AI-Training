

while(True):
    amount = int(input("enter purchase amount : "))
    if(amount < 0): break
    if(amount > 1000): print(f"the purchase amount is : {amount}")
