# Move all zeores to the end without alterning the relative order of the array

nums = [0, 5, 0, 8, 3, 0, 9, 2]
print(nums)

j, i = 1, 0


while i < len(nums) and j < len(nums):
    if nums[i] != 0:
        i += 1
        if i >= j:
            j += 1
    elif nums[i] == 0 and nums[j] == 0:
        j = j + 1
    elif (j < len(nums) and nums[i] == 0 and nums[j] != 0):
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j + 1

print(nums)
