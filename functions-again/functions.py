
# files="hamza files"
# def myName(xyz): # name parameter
#     # print(xyz)
#     # files="waqas files"
#     print(files)


# abc="para"
# myName(abc)    #  name argument

# name="ali khan"

# def myName():
#     name="ali"
#     # print(name)
#     return name
#     # pass

# # name="waqas"  
# name=myName()  
# print(name)

# n=7
# for i in range(2,n):
#     isPrime=True
#     if n%i ==0:
#         print("not prime number ")
#         isPrime=False
#         break
#     return isPrime   

def isPrime(n):
    prime=True
    for i in range(2,n):
        if n%i ==0:
            prime=False
            break
    return prime 

while True:
    uerInput=int(input("Enter a numbre to check that the number is prime or not :"))
    result=isPrime(uerInput)
    print(result)  
    if result:
        print( "your given number is Prime number") 
    else:
        print("your given number is not a prime number")    

    runAgain=input("Do you want to check another number (y/n) :")  
    if runAgain.lower()=="n":
        print("Thank you ")
        exit()  