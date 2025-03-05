# program number 10
# number=0 #1
# while number<90:
#     number+=1
#     print(number)
# program no 11
# number=int(input("Enter a number  "))
# sum=0
# for i in range(1,number+1):
#     sum +=i
# print(f"your number sum is equal is {sum}")

# program number 12

#what is your name
# number=int(input("Enter your number to generate a tabel :")) # 2
# for i in range(1,11):
#     print(f'{number}X{i}={number*i}')
#
# list=[1,2,3,4,5,6,7,8,9]
# list.reverse()
# print(list)

# list_name=["alikhan","zaryab","zaryan","ahmad"]
# list_name.reverse()
# print(list_name)

# list=[]
# for i in range(5):
#     fruits=input("Enter here the name of fruits that you like the most: ")
#     list.append(fruits)
# print(list)
#

# list = []
# exicution=False
# while not exicution:
#     fruits = input("Enter here the name of fruits that you like the most: ")
#     want_to_continue=input("Do you want to continue (yes/no)")
#     if want_to_continue == "no":
#         exicution=True
#     list.append(fruits)
# print(list)

# list=[11,12,13,14,15,16,17,18,19]
# print(list)
# squre_list=[]
# for i in list:
#     square=i**2
#     squre_list.append(square)
#
# print(squre_list)





def max_of_list(list):
    mx=list[0]
    for a in list:
        if a > mx:
            mx=a
    return mx


max_number=max_of_list([34,54,56,23,21,78,87,90,1,3,78,45])
print(f"from your list this is the maximum number {max_number}")


def average(list):
    total=0
    lenght=0
    for a in list:
        total+= a
        lenght+=1
    return total/lenght
result=average([34,54,56,23,21,78,87,90,1,3,78,45])

def average(list):
    total=0

    for e,a in enumerate(list):
        total+= a
    return total/(e+1)
result=average([34,54,56,23,21,78,87,90,1,3,78,45])





def standarddeviation(list):
    N=len(list)
    meo=average(list)
    diff=0
    for x in list:
        diff+=(x-meo)**2
    return (diff)**(1/2)

res=standarddeviation([34,54,56,23,21,78,87,90,1,3,78,45])
print(res)

# file read Write
open()
# f.read()
# f.close()
# f.seek()

# we can perform same work as it is with open()
# but we don't have to close the file again
# once we close the file then we con't access the file
# try exept syantax









