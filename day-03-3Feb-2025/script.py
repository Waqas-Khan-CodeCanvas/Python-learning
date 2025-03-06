# lang = input("What's the programming language you want to learn? ")

# match lang:
#     case "JavaScript":
#         print("You can become a web developer.")

#     case "Python":
#         print("You can become a Data Scientist")

#     case "PHP":
#         print("You can become a backend developer")

#     case "Solidity":
#         print("You can become a Blockchain developer")

#     case "Java":
#         print("You can become a mobile app developer")
#     case _:
#         print("The language doesn't matter, what matters is solving problems.")

# day = input("Enter a day of the week: ")

# match day:
#     case "Monday":
#         print("It's the start of the work week.")
#     case "Tuesday":
#         print("It's Tuesday.")
#     case "Wednesday":
#         print("It's Wednesday.")
#     case "Thursday":
#         print("It's Thursday.")
#     case "Friday":
#         print("It's Friday, almost the weekend!")
#     case "Saturday":
#         print("It's the weekend!")
#     case "Sunday":
#         print("It's Sunday, the end of the weekend.")
#     case _:
#         print("That's not a valid day of the week.")

# if else validation simple 
# name=input("Enter your name : ")
# new_name=name.lower().strip()

# print(name.upper())
# print(name.capitalize())
# if new_name=="ali":
#     print("yes your name is ali")
# else:
#     print("who are you")    
# name = name.strip()

# simple programe to check that the character intered by the user is in upper case or lower case

# char=input("Enter a single character here : ")
# if char.isalpha():
#     if char.islower():
#         print(f"the character is : {char} lower case")
#     else:
#         print(f"the character is : {char} upper case")
# else:
#     print(f"invalid character : {char}")  


# age=int(input("Enter your age : ")) 
# if age!=0 and age<0:
#     if age >=30:

from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

DOB = date(1990, 1, 1)  # Example date of birth
age = calculate_age(DOB)
print("Age:", age)