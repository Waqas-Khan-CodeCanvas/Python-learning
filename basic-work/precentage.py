marks=int(input("Enter your marks here:"))

total=600
percentage=round((marks/total)*100)

print(f"total marks is {total}")
print(f"your obtain  marks is {marks}")
# print(f"your percentage  marks is {percentage}")
if percentage<=60:
    print(f"you current percentage is {percentage}% ")
    print("this is a normal  percentage")
elif percentage<=80:
    print(f"you current percentage is {percentage}%  ")
    print("This is a good percentage")
elif percentage<=90:
    print(f"you current percentage is {percentage}%  ")
    print("this is a best percentage")
elif percentage<=100:
    print(f"you current percentage is {percentage}%  ")
    print("this is an Exellent percentage")
else:
    print(f"wrong data {marks}")
print("thanks")
print("good bye")