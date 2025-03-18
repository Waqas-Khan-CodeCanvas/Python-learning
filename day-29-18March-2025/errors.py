def binary_search(list, userinput):
    lower = 0  
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2  
        if list[mid] == userinput:
            return True
        else:
            if list[mid] < userinput:
                lower=mid
            else:
                upper = mid
                
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# userinput = int(input("Enter a number you want to find from the list: "))\
user_input=2    
if binary_search(list,user_input):
    print(" Element is found")
else:
    print("Element is not found")    