dict1 = {
    "1": "apple",
    "2": "banana"
}

list1 = ["apple","banana","orange","mango"]
list2 = []
print(list1)
dict2 = {}
#second letter
list3 = []
for i in range(len(list1)):
    a = list2.append(list1[i][1:2])
    dict2[a] = list1[i]
    list3.append(list1[i][len(list1)-1:len(list1):])
    
print(dict)
#accessing the second letter
# print(sorted(list2))

#accessing the second last letter
# print(sorted(list3))


list5 = ["apple", "banana", "orange", "mango"]

n = len(list5)

for i in range(n):
    for j in range(n - i - 1):
        if list5[j][1] > list5[j + 1][1]:  # Compare second letters
            list5[j], list5[j + 1] = list5[j + 1], list5[j]

print(list5)


