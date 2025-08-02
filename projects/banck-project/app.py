def registerUser():
    userName = input("Enter your user Name : ")
    userEmail = input("Enter your Email : ")
    userPassword = input("Enter your Password : ")
    userPhone = input("Enter your P. No : ")
    userAddress = input("Enter your Address : ")
    initialBalance = input("Enter some Amount of money : ")

    userData = open(userName, "w")
    userData.write(userName + " ")
    userData.write(userPassword + " ")
    userData.write(userEmail + " ")
    userData.write(userPhone + " ")
    userData.write(userAddress + " ")
    userData.write(initialBalance)
    print(f"Hi {userName}, your Account has been created.")
    return True


data=[]
def login():
    userName = input("Enter your user Name : ")
    userPassword = input("Enter your Password : ")

    try:
        userData = open(userName, "r")
        userData = userData.read()
        userDataList = userData.split()
    except FileNotFoundError:
        print("User not found. Please register first.")
        return False
    
    userAuth = False
    if userName == userDataList[0]:
        if userPassword == userDataList[2]:
            userAuth = True
            for i in userDataList:
                data.append(i)
        else:
            print("Invalid User Password. please try again!")
    else:
        print("Invalid User Name. please try again!")
    
    return userAuth

print("Welcome to our store")

while True:
    print("""
        1: SignUp
        2: Login
    """)
    
    userLogin = input("Enter your choice : ")
    
    if userLogin == "1":
        userAuth = registerUser()
    elif userLogin == "2":
        userAuth = login()
        break
    else:
        print("Invalid input please try again! ")

def showProfile():
    print(f"""
          Account Holder Name : {data[0].capitalize()}
          Account Holder Email : {data[1]}
          Account Holder Ph.No : {data[3]}
          Account Holder Address : {data[4].capitalize()}
          Account Current Balance : {data[5]}
        """)
    
def checkBalance():
         print(f"""
          Account Holder Name : {data[0].capitalize()}
          Your Current Balance : {data[5]}
        """)
         
def depositMoney():
    print(f" Your Current Balance : {data[5]}")
    depositMoney=int(input("Enter your amount to deposit :"))
    if depositMoney > 0:
        currentBalance=int(data[5])+depositMoney
        print(f"Money has been deposited {depositMoney} ")
        print(f"Your Total Balance is : {currentBalance} ")
        data[5]=str(currentBalance)
        userData = open(data[0], "w")
        for i in data:
             userData.write(i + " ")
    else:
        print("Invalid Amount Entered!")    

def withdraw():
    print(f" Your Current Balance : {data[5]}")
    withdraw=int(input("Enter your amount to withdraw :"))
    if withdraw < int(data[5]):
        currentBalance=int(data[5])-withdraw
        print(f"Money has been withdraw {withdraw} ")
        print(f"Your Remaining Balance is : {currentBalance} ")
        data[5]=str(currentBalance)
        userData = open(data[0], "w")
        for i in data:
             userData.write(i + " ")
    else:
        print("Insufficient  Amount! In your Account ")    

def resetPassword():
    print(" Reset Your Password here .......")
    userName=input("Enter Account User Name : ")
    if userName == data[0]:
        newPassword=input("Enter Your New Password : ")
        data[2]=newPassword
        userData = open(data[0], "w")
        for i in data:
             userData.write(i + " ")
        print("Your Password has been updated.")     
    else:
        print("Invalid User Name please try Again..")    
    
def logout():
    print("Thank you for using  UBL Banking System")
    exit()

print(data)

if userAuth:
    print("""
        1: Show Profile
        2: Check Balance
        3: Deposit Money
        4: Withdraw Money
        5: Reset Password
        6: Logout
    """)
#     
    userChoice = input("Enter your choice : ")
    if userChoice == "1":
        showProfile()
    elif userChoice == "2":
        checkBalance()
    elif userChoice == "3":
        depositMoney()
    elif userChoice == "4":
        withdraw()
    elif userChoice == "5":
        resetPassword()
    elif userChoice == "6":
        logout()