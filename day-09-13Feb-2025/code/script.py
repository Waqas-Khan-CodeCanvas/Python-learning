# list upaking in python

# names=["ali","hamza","sufyan","waqas","zaryab"]

# firstname,secondname,thirdname=names
# firstname, *othernames=names
# firstname,*othernames,lastname=names

# print(firstname)
# print(othernames)
# print(lastname)


# list function
# names=["ali","hamza","sufyan","waqas","zaryab"]
# use the following function on list

    # .remove()
    # .pop()
    # .copy()
    # .reverse()
    # .min()
    # .max()
    # .append()
    # .insert()
    # .extend()
    # .sort()

# generatiing a list of number or characters
# numbers=list(range(100))
# print(numbers)   

# alphabets=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# print(alphabets)

# numbers=list(range(1,50))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(numbers)
# for index , number in enumerate(numbers):
#     # print(number[0], number[1])
#     print(index , number)

numbers=list(range(1,50))
alphabets=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters=list("!@#$%^&*())_+")

for number,alpha,special in zip(numbers, alphabets, special_characters):
    print(number**2 ,alpha,special)

