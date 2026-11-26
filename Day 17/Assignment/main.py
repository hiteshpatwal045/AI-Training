nums = [10, 20, 30, 20, 40, 50, 20, 40, 10, 20, 30, 30]
print(f"Original Array: {nums}")


# Delete the first 20 by value.
# arr = nums
# arr.remove(20)
# print(f"after remove the first 20: {arr}")

# Delete the element at index 2 and store the deleted value in removed.
# arr = nums
# removed = arr.pop(2)
# print(f"Removed value {removed} \nAarray after removing index value2 {arr}")

# Delete elements from index 1 through 2 using del.
# arr = nums
# del arr[1:2]
# print(arr)


# Delete all remaining elements without deleting the data variable.
# arr = nums
# arr.clear()
# print(arr)


# Check whether 40 exists.
# if 40 in nums:
#     print("Yes")
# print("No")

# Check whether 100 does not exist.
# if 100 not in nums:
#     print("No")
# print("Yes")

# Find the first index of 30.
print(nums.index(30))

# Count how many times 30 occurs.
print(nums.count(30))

# Without using index(), print all indexes where 30 occurs.
# for i in range(len(nums)):
#     if(nums[i] == 30):
#         print(f"30 is present at index {i}")


for ind, val in enumerate(nums):
    if val == 30:
        print(f"{val} found at index: {ind}")
