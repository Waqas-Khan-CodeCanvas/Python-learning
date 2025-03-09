from twilio.rest import Client
def send_sms():
    

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='',
    body='thank you for using our calculaiton system',
    to=''
    )
    print(message.sid)

def addition(num1,num2):
    result=num1+num2
    return result

def subtraction(num1,num2):
    result=num1-num2
    return result

def multiplication(num1,num2):
    result=num1*num2
    return result

def division(num1,num2):
    result=num1/num2
    return result

run=True
while run:
    print("\t1 :- Addition ")
    print("\t2 :- Subtraction ")
    print("\t3 :- Multiplication ")
    print("\t4 :- Division ")

    user_choice=int(input(("Enter your choice here : ")))
    if user_choice >= 1 and user_choice <=4 :
        first_number=int(input("Enter Your first  Number here : "))
        second_number=int(input("Enter Your second  Number here : "))
    else:
        print("Ivalid input")  
        exit()

    if user_choice == 1:
        result=addition(first_number,second_number)
        print(f"Sum of the given numbers is : {result}")

    elif user_choice == 2:    
        result=subtraction(first_number,second_number)
        print(f"Difference of the given numbers is : {result}")

    elif user_choice == 3:    
        result=multiplication(first_number,second_number)
        print(f"Product of the given numbers is : {result}")

    else :    
        result=division(first_number,second_number)
        print(f"Division of the given numbers is : {result}")

    exit=input("Do your want to exit (y/n)") 
    if exit.lower()=="y":
        run=False   

print("Thank your!")
send_sms()
if __name__ == "__main__":
    send_sms()