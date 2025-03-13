data={"name":"hamza","marks":"900","class":"12th","grade":"A"}
# print(data)
# print(data.keys())
# print(data.values())
# print(data.items())
print(data["name"])
print(data.get("name"))
print(data.get("hello","item not found"))

# for i in data:
#     print(i)

# for i in data:
#     print(data[i])

# for i in data:
#     print(i ," -> " ,data[i])

# for i in data.keys():
#     print(i)

# for i in data.values():
#     print(i)

for i, j in data.items():
    print(i ," -> " ,j)
    
        
# name=6
# print(6 is name)

# name="hamza"
# ali="ali"

# print(ali is name)
# print(name==ali)
# x = 300
# y = 300

# print(x == y)  # True, because values are equal
# print(x is y)  # False, because Python does not cache large integers
# Difference Between is and == in Python
# In Python, is and == are used for different purposes:

# == (Equality Operator) checks if values of two variables are equal.
# is (Identity Operator) checks if two variables point to the same object in memory