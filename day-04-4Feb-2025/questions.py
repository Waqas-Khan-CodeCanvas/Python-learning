# Write a program to check whether a number is negative, positive or zero. 
# 
# number = int(input("Enter a number to check that a number is negative, positive or zero :"))
# if number!=0:
#     if number >0:
#         print(f" the given number is positive {number}")
#     else:
#         print(f" the given number is negative {number}")
# else:
#     print(f" the given number is zero {number}")

# Write a program to check whether a number is divisible by 5 and 11 or not    # 
# Write a program to check whether a number is even or not.
# as task to you

# Write a program to check whether a character is alphabet or not
# char=input("Enter an alphabet here : ")
# if char.isalpha():
#     print(f" the character is alphabet {char}")
# else:
#     print(f" the character is not an alphabet {char}")



# Write a program to check whether a character is uppercase or lowercase alphabet
# char=input("Enter an alphabet here : ")

# if char.islower():
#     print(f" the character is lower case alphabet {char}")
# elif char.isupper():
#     print(f" the character is upper case alphabet {char}")
# else:
#     print(f" invalid input {char}")



# Write a program that calculates product of odd integers from 1 to 15 using loop. 
# sum_of_odd=0
# for i in range(16):
#     if i%2!=0:
#         sum_of_odd+=i
        
# print(f"sum of odd number from 1 to 15 is : {sum_of_odd}")



# Write a program that inputs a series of 5 numbers from user and determines and prints largest number, using loop.

# name="ali hamza sufyan waqas hasham"
# names=name.split(" ")
# print(name)
# print(names)

numbers=input("Enter a serise of 5 numbers : ") # 100 200 300 400 500
print(numbers)
number_list=numbers.split(" ") # ['100', '200', '300', '400', '500']
print(number_list)

int_list=[]

for i in number_list:          # ['100', '200', '300', '400', '500']
    int_list.append(int(i))

# print(int_list)
# print(max(int_list))
    
max_number=int_list[0]

for i in int_list:   # [100, 200, 300, 400, 500]
    if i > max_number:
        max_number=i

print(max_number)