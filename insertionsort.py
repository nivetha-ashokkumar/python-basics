list1 = [20, 10, 25, 15, 30]
print("unsorted list:", list1)
    
for i in range(1, len(list1)):
        if list1[i - 1] > list1[i]:
            list1[i], list1[i - 1] = list1[i - 1],list1[i]
            
print("sortd list:", list1)