
for idx in range(1,501):
    if idx % 41: 
        break
    if idx % 6 == 0:
        continue
    if idx % 2 == 1:
        print(idx)
