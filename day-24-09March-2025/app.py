# try:
#     number =10
#     number2 = 0
#     result = number / number2
#     print(result)
# except:
#   print('zero divition error')

# print("This is the continue of the program")

# try:
#     number = 10
#     number2 = 0
#     result = number / number2
#     print(result)
# except (ZeroDivisionError, ValueError):
#     print(ZeroDivisionError,ValueError)
# finally:
#     print("This is the continuation of the program")
    
# print("This is the continuation of the program")    


# Example 1: Handling multiple exceptions
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range")
except Exception as e:
    print(f"An error occurred: {e}")

print("hello")
# Example 2: Handling file operations
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except IOError:
    print("An I/O error occurred")

# # Example 3: Handling type errors
try:
    result = 'string' + 10
except TypeError:
    print("Type error: cannot concatenate 'str' and 'int'")

# # Example 4: Handling custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught custom error: {e}")

# # Example 5: Handling value errors
try:
    number = int("not_a_number")
except ValueError:
    print("Value error: invalid literal for int()")