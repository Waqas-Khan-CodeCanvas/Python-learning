# print("hello world")
# if True:
#     print("print")

# greet()
# number ="5"+5
# print(number)
# numbers=[1,2,3,4,5,6,7]
# print(numbers[10])

# def greet(name):
#     print(name+" hello")

# greet()
# def find_first_repeating(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 return arr[i]  # Should return the first repeating number
#     return -1  # No repeating number found

# # Test cases
# print(find_first_repeating([3, 1, 4, 5, 3, 6, 4]))  # Expected: 3
# print(find_first_repeating([1, 2, 3, 4, 5]))        # Expected: -1
# print(find_first_repeating([7, 8, 9, 8, 7]))        # Expected: 7 (but might return 8 due to logic error)


# def find_largest(arr):
#     largest = arr[0]
#     for num in arr:
#         if num > largest:  
#             largest = num
#         else:
#             largest = largest
#     return largest

# # Test cases
# print(find_largest([3, 1, 4, 5, 2]))  # Expected: 5
# print(find_largest([10, 20, 5, 8, 30]))  # Expected: 30
# print(find_largest([-1, -5, -3, -8, -2]))  # Expected: -1

# try:
#     text=open("helloworld.txt")
#     print(text.read())
#     # print(10/0)
  
# except:
#   print('An exception occurred file not found')


# print("welcome to the site")

# ********
# ********
# ********
# ********
# while True:
n=int(input("Enter a number here : "))

for i in range(1,n+1):
        print("* "* n)
userChoice=input("Do you want to try again : (y/n)")  
if userChoice.lower()=="n": 
        exit() 

# n=int(input("Enter a number here : "))
# while n > 0:
#     print("* "* n) 

    