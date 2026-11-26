# 3. Identify all missing numbers between the smallest and the largest numbers
nums = [1,3,5,6,9,10,12]

largest, smallest, n = max(nums), min(nums), len(nums)

missing_numbers = []
for i in range(smallest,largest+1):
    if i not in nums:
        missing_numbers.append(i)

print(missing_numbers)
