def registerUser():
    userName=input("Enter your user  Name : ")
    userEmail=input("Enter your Email : ")
    userPassword=input("Enter your Password : ")
    userPhone=input("Enter your P.No : ")
    useraddress=input("Enter your Address : ")
    intintilaBalalance=input("Enter some Amount of money : ")
    
    userData=open(userName, "w+")
    userData.write(userName+" ")
    userData.write(userPassword+" ")
    userData.write(userEmail+" ")
    userData.write(userPhone+" ")
    userData.write(useraddress+" ")
    userData.write(intintilaBalalance+" ")
    print(f"Hi , {userName} your Account has been created.")
    return True

data=[]
def login():
    userName=input("Enter your user Name : ")
    userPassword=input("Enter your Password : ")
    userAuth=False
    
    filsData=open(userName,"r")
    userCredentials=filsData.read()
    userCredentials=userCredentials.split()
    if userName ==userCredentials[0]:
        if userPassword == userCredentials[1]:
            userAuth=True
            for i in userCredentials:
                data.append(i)
        else:
            print("Invalid User Password. please try again!")    
    else:
        print("Invalid User Name. please try again!")
    return userAuth

print("Welcome to our Bank Simulation Machine! ")
userAccess=False
while True:  
    print("""
            1 :- SignUp
            2 :- login
    """)
    userLogin=input("Enter your choice : ")
    if userLogin=="1":
        userAccess=registerUser()
        if userAccess:
            break
    elif userLogin=="2":
        userAccess=login()
        if userAccess:
            break
    else:
        print("Invalid input please try again! ")

def showProfile():
    print(f"""
          Account Holder Name : {data[0]}
          Account Holder Email : {data[2]}
          Account Holder P.No : {data[3]}
          Account Holder Address : {data[4]}
          Account Current Balance : {data[5]}
    """)
    
def checkBalance():
    print(f"""
            Account name : {data[0]}
            Account Balance : {data[5]}
        """)    

def depositMoney():
    print(f"Your Account Current Balance is : {data[5]}")
    depositMoney=int(input("Enter your amount to deposit : "))
    if depositMoney > 0:
        newBalance=int(data[5])+depositMoney
        data[5]=str(newBalance)
        userCredentials=open(data[0],"w")
        for i in data:
            userCredentials.write(i+" ")
    else:
        print("Invalid Amount Entered..") 

def withdrawMoney():  
    print(f"Your Account Current Balance is : {data[5]}")
    withdrawMoney=int(input("Enter your amount to Withdraw : "))
    if withdrawMoney < int(data[5]):
        newBalance=int(data[5])-withdrawMoney
        data[5]=str(newBalance)
        userCredentials=open(data[0],"w")
        for i in data:
            userCredentials.write(i+" ")
    else:
        print("Invalid Amount Entered..")              

def resetPassword():
    print("Reset your Password ")
    oldPassword=input(f"{data[0]} Enter Your Account Current Password : ")
    
    if oldPassword == data[1]:
        newPassword=input("Enter your New Password: ")
        data[1]=newPassword
        userCredentials=open(data[0],"w")
        for i in data:
            userCredentials.write(i+" ")
    else:
        print("Invalid Password ..") 

def logout():
    print(f" Thank you {data[0]} \n Good by...")
    exit()
if userAccess:
    while True:
        print("""
            1:- Show Profile 
            2:- Check Balance 
            3:- Deposit Money 
            4:- Withdraw Money 
            5:- Reset Password 
            6:- Logout 
            """)   
        userChoice=input("Enter your choice : ")
        if userChoice=="1":
            showProfile()
        elif userChoice=="2":
            checkBalance()
        elif userChoice=="3":
            depositMoney()
        elif userChoice=="4":
            withdrawMoney()
        elif userChoice=="5":
            resetPassword()
        elif userChoice=="6":
            logout()
        
