# def linear_search(arr, target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index
#     return -1

# # Example
# arr = [10, 23, 45, 70, 11, 15]
# target = 70

# result = linear_search(arr, target)

# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found in the array")


# linear searching in python
# def search(list,n):
#     for i in range(len(list)):
#         if list[i]==n:
#             return True


# list =[1,2,3,4,5,6,7,8]
# n=4
# if search(list,n):
#     print("item found")
# else:
#     print("item not found ")

list=[1,23,3,4,5,6,87]
found=False
n=4   # we can add user Input here 
for i in range(len(list)):
    if list[i] == n:
        found=True
if found:
    print("item is found")
else:
    print("item not found ")    