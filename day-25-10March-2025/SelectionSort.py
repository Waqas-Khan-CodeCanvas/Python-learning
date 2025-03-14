# Selection Sorting in python

numbers=[6,4,7,8,2,3,1]

for i in range(len(numbers)):
    min_index=i
    # print(min_index)
    for j in range(i,len(numbers)):
        # print(j)
        if numbers[j] < numbers[min_index]:
            min_index=j
    numbers[i],numbers[min_index]=numbers[min_index],numbers[i]
    # temp=numbers[i]
    # numbers[i]=numbers[min_index]
    # numbers[min_index]=temp
    
print(numbers)            