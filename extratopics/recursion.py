
# # print("hello world")
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# # recursion 
# count = 0 
# def sayHello():
#     global count
#     print(f"hello {count}")
#     count+=1
#     sayHello()
# sayHello()    


# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# result = factorial(5)
# print(result)

# 5x4x3x2x1

# try:
#     user_input= int(input("Enter a number to add with 2 :"))
#     print(2 - user_input)
# except ValueError as e:
#     print("Invalid Input",e)
        
# print("byee")        

# try:
#   print(x)
# except:
#   print('An exception occurred')
try:
    file=open("hello.txt","r")
    file.read()
    print(file)
except IOError as  e:
    print("error occuerd",e)
    
    
print("byee")



