numbers=input("Enter your number here:")

list=numbers.split()

int_list=[]
for i in list:
    int_list.append(int(i))

print(int_list)
maximum_number=int_list[0]

for i in int_list:
    if i > maximum_number:
        maximum_number = i


print(f"the maximum number in the list is {maximum_number}")