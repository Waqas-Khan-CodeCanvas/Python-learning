# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # Output: 120

def name():
  count = 0
  pr = True
  while pr:
    print("hello world")
    count +=1
    if count >= 10:
      pr = False
    else:
      name()  

name()