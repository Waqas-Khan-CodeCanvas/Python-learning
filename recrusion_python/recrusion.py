# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


# count = 0
# def greet():
#     global count
#     count+=1
#     print("hello ",count)
#     greet()
    
# greet()    


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result  = factorial(5)
print(result)