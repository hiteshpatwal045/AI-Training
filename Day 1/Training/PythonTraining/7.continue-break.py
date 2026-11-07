
print("--------------FIRST_PROGRAM------------")

for idx in range(1,10):
    if(idx == 2 or idx == 4):
        continue
    else:
        print(idx)


print("--------------SECOND_PROGRAM------------")

for idx in range(1,10):
    if(idx == 2 or idx == 4):
        break
    else: 
        print(idx)
