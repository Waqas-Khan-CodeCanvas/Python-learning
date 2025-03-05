even=[]
odd=[]
sum_of_even=0
sum_of_odd=0
sum=0
for i in range(1,101):
    sum +=i
    if i % 2 ==0:
        even.append(i)
        sum_of_even +=i
    else:
        odd.append(i)
        sum_of_odd += i
print(f"This is the list of all even  number from 1 to 100 : {even} ")
print(f"This is the list of all odd  number from 1 to 100 : {odd} ")
print(f"This is the sum of all  number from 1 to 100 : {sum_of_even} ")
print(f"This is the sum of all odd  number from 1 to 100 : {sum_of_odd} ")
print(f"This is the sum of all number from 1 to 100 : {sum} ")
