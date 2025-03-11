
# def create_stack():
#         stack=[]
#         return stack

# def push(stack,item):
#     stack.append(item)
#     return stack 


# def check_empty(stack):
#       return len(stack)


# def pop(stack):
#       if len(stack)<1:
#             print("stack is empty")
#       else:
#         stack.pop()
            
# fruit=create_stack()
# veg=create_stack()
# cosm=create_stack()
# Kitchen=create_stack()
# bakery=create_stack()








# # while True:
# #     print("Welcome to our python program Create a stack ")
# #     stackName=input("Enter your Stack name here  : ")
# #     stackName=create_stack()
# #     stackElement=input

# #     if user_input == "pop":
# #       stack=pop(stack)
# #     elif user_input:
# #       stack=push(stack,user_input)
# #       print(stack)
# #     else:
# #       print("invalid input")
      
# #     print(stack)
# #     runAgain=input("Do you want to check another number (y/n) :")  
# #     if runAgain.lower()=="n":
# #        print("Thank you ")
# #        exit()
fruit=["mango","apple","lichi","banana","orange"]
vege=["tomato","potato","onion","ladifinger","caret"]
cons=["creem","shampo","makupe","facewash","comb"]
kitchen=["knife","spoon","sputula","cooker","oven"]
bakery=["samosa","donuts","biscuit","creemrolls","pizza"]

def printItems(itemList):
    count=1
    for i in itemList:
        print("\t",count," :- ",i)
        count+=1

print("Welcome to our Store")
print("""
        1 :- Fruits 
        2 :- Veg
        3 :- cosm
        4 :- Kitchen
        5 :- bakery
""")
while True:
    userInput=int(input("Enter what you need : "))
    if userInput== 1:
        printItems(fruit)
        
    elif userInput== 2:
        printItems(vege)
    elif userInput== 3:
        printItems(cosm)
    elif userInput== 4:
        printItems(kitchen)
    elif userInput== 5:
        printItems(bakery)
    else:
        print("Invalid input")  

    runAgain=input("Do you want to buy more : (y/n)")  
    if runAgain.lower() == "n":
        print("Thank you for visiting our store") 
        exit()   

     
