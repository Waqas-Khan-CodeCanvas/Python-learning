import array

# import array

# print("hello world! I am Array.py")
# myArray=array.array('i',[1,2,3,4,5,6,7,8,9,10])
# myArray2=array.array('u','ali')
# print(type(myArray))
# print(myArray)
# print(myArray2)

# myStringArray = array.array('u', 'hello world')
# print(myStringArray)





# Create an array of integers
myArray = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Append a new element to the array
myArray.append(11)
print("Array after appending 11:", myArray)

# Insert a new element at a specific position
myArray.insert(0, 0)
print("Array after inserting 0 at position 0:", myArray)

# Remove an element from the array
myArray.remove(5)
print("Array after removing 5:", myArray)

# Pop an element from the array
popped_element = myArray.pop()
print("Popped element:", popped_element)
print("Array after popping an element:", myArray)

# Get the index of an element
index_of_7 = myArray.index(7)
print("Index of element 7:", index_of_7)

# Reverse the array
myArray.reverse()
print("Array after reversing:", myArray)

# Count occurrences of an element
count_of_2 = myArray.count(2)
print("Count of element 2:", count_of_2)

# Create an array of unicode characters
namesArray = array.array('u', 'alihamzakhanwaqas')
print("Names array:", namesArray)