
def create_stack():
        stack=[]
        return stack

def push(stack,item):
    stack.append(item)
    return stack 


def check_empty(stack):
      return len(stack)


def pop(stack):
      if len(stack)<1:
            print("stack is empty")
      else:
        stack.pop()
            



while True:
    print("Welcome to our python program Create a stack ")
    stackName=input("Enter your Stack name here  : ")
    stackName=create_stack()
    stackElement=input

    if user_input == "pop":
      stack=pop(stack)
    elif user_input:
      stack=push(stack,user_input)
      print(stack)
    else:
      print("invalid input")
      
    print(stack)
    runAgain=input("Do you want to check another number (y/n) :")  
    if runAgain.lower()=="n":
       print("Thank you ")
       exit()

