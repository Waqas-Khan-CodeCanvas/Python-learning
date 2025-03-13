# print("hello wrold")

# myDictionary={ "name":"ali","class":"12th","grade":"D","city":"Bannu"}

# print(myDictionary["class"]) # access values
# myDictionary["marks"]="900" # add element to the dictionary
# myDictionary["class"]="BSAI" # update element in the dictionary
# del myDictionary["city"]    # delete element from the dictionary

# print(myDictionary)

# # looping over the dictionary
# myDictionary={ "name":"ali","class":"12th","grade":"D","city":"Bannu"}

# for item in myDictionary:           # general loop over dictionary
#     print(f"{item} is : {myDictionary[item]}") 

# for keys in myDictionary:
#     print(keys)

# for value in myDictionary.values():
#     print(value)

# for item in myDictionary.keys():
#     print(item)

# for key ,value  in enumerate(myDictionary):
#     print(key , value)  

# copyDictionary=myDictionary.copy()

# copyDictionary["name"]="waqas"
# print(myDictionary)
# print(copyDictionary)

# how to convert two list into a single dictionary
# fruits=["apple","bananas","cherry","mango","orange"]
# prices=[100,200,300,400,500]

# items={}
# # items["whatmelan"]=800
# for i in range(5):
#     items[fruits[i]]=prices[i]

# print(items)

# items={}
# for i,j in zip(fruits,prices):
#     items[i]=j
    
# print(items)

# get method for dictionary
# myDictionary={ "name":"ali","class":"12th","grade":"D","city":"Bannu"}

# print(myDictionary.get("name"))
# print(myDictionary["hello"])
# print(myDictionary.get("name","item not found"))
# myDictionary.clear()
# print(myDictionary)

students={
    "hamza":{ "name": "hamza","marks":"900","class":"12th","grade":"A"},
    "sufyan":{ "name": "sufyan","marks":"90","class":"12th","grade":"u"},
    "zaryab":{ "name": "zaryab","marks":"700","class":"12th","grade":"B"},
    "waqas":{ "name": "waqas","marks":"689","class":"12th","grade":"A"},
    "ali":{ "name": "ali","marks":"976","class":"12th","grade":"A"},
    "hasham":{ "name": "hasham","marks":"876","class":"12th","grade":"A"}
}

# Looping over the dictionary
# print("Looping over the dictionary:")
# for student in students:
#     print(f"{student} details: {students[student]}")

# Looping over keys
# print("\nLooping over keys:")
# for key in students.keys():
#     print(key)

# # Looping over values
# print("\nLooping over values:")
# for value in students.values():
#     print(value)

# Looping over items
# print("\nLooping over items:")
# for key, value in students.items():
#     # print(f"{key}: {value}")
#     for i,j in value.items():
#         print(f" {i} -> {j}  ")
#     print("\n")    

# Enumerating over the dictionary
# print("\nEnumerating over the dictionary:")
# for index, (key, value) in enumerate(students.items()):
#     print(f"{index}: {key} -> {value}")

# print(students)
# for i in students:
#     item=students[i]
#     for j in item:
#     print(j)
