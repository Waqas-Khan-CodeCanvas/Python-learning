# Bubble Sort in python DSA
numbers = [5, 2, 9, 1, 5, 6]
for i in range(len(numbers)-1,0,-1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            # temp=numbers[j]
            # numbers[j]=numbers[j+1]
            # numbers[j+1]=temp


print(numbers)            

# a,b,c=1,2,3
# print(a,b,c)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Bubble Sorted list:", sorted_numbers)