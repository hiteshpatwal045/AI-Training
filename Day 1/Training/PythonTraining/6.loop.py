cntEven, sumEven, cntOdd, sumOdd = 0, 0, 0, 0

for idx in range(0,50):
    if(idx % 2 == 0):
        cntEven += 1
        sumEven += idx
        print(idx)

print(f"Sum of even Number : {sumEven}")
print(f"Total num of even Number : {cntEven}")


for idx in range(0,50):
    if(idx % 2 == 1):
        cntOdd +=1
        sumEven += idx
        print(idx)

print(f"Sum of Odd Number : {sumOdd}")
print(f"Total num of Odd Number : {cntOdd}")


cntBoth, sumBoth = cntOdd+cntEven, sumEven + sumOdd

print(f"Cnt of Both Num : {cntBoth}")
print(f"Sum of Both Num : {sumBoth}")
print(f"Avg of Both Num : {sumBoth/cntBoth}")


for idx in range(1,9):
    print(idx)

for idx in range(1,20,2):
    print(idx)