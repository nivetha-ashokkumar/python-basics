list1 = [20, 10, 25, 15, 30]
print("unsorted list:", list1)

for j in range(len(list1) - 1):
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1],list1[i]
            
print("sortd list:", list1)