number = input("Enter a list of number here:")
print(f"The user input is: {number}")
# to convert user input into list
list = number.split()
print(f"The number list is: {list}")
# to convert string list into interger list
integer_list = []
for i in list:
    integer_list.append(int(i))
print(f"The integer list is: {integer_list}")
# to find sum of all the numbers
total = 0
for i in integer_list:
    total += i
print(f"The sum is: {total}")
# to find the lenght of the list
length = 0
for i in integer_list:
    length += 1
print(f"The length is: {length}")
# to find the average of the list
avg = round(total/length)
print(f"The average is: {avg}")





