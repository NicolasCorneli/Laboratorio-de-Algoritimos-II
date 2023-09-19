list1 = [2,1,0,6,5,4,3,7,9,8]
for i in range(len(list1)):
    print(list1)
    for x in range(len(list1)):
        if list1[i] < list1[x]:
            v = list1[i]
            z = list1[x]
            list1[i] = z
            list1[x] = v
print(list1)
