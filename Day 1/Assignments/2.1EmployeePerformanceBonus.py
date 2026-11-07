empRating = int(input("enter rating"))
empExp = int(input("enter experience"))
empProStatus = input("enter Project status")

bonus = 0

if empRating >= 5 and empExp > 10 and empProStatus == "on time":
    bonus = 30
elif empRating == 4 and empExp > 7:
    bonus = 20
elif empRating == 3 and empProStatus == "delayed":
    bonus = 5
else:
    bonus = 0

print(f"The curr emp recieved a bonus of : {bonus}%")