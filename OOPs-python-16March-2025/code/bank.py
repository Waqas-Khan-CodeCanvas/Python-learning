class Account:
    def __init__(self,name,balance,account_no):
        self.name=name
        self.balance=balance
        self.account_no=account_no
        
    def deposity(self,amount):
        self.balance+=amount
        print(f"Account number is {self.account_no}")
        print(f"Rs {amount} is deposited. ")
        print(f"{self.name} your current balance is {self.get_balance()} \n")    
        
    def withdraw(self,amount):
        self.balance -= amount
        print(f"Account number is {self.account_no}")
        print(f"Rs {amount} is withdraw. ")
        print(f"{self.name} your current balance is {self.get_balance()} \n")   
    
    def get_balance(self):
        return self.balance   
    print("this is the flow of how the programe is working in real world this is show how to work with real life senario you that this is the process of how")
    
    
hamzaAccount=Account("hamza",10000,45678) 
sufyanAccount=Account("sufyan",20000,98765) 
waqasAccount=Account("waqas",30000,12456) 

hamzaAccount.withdraw(1000)    
sufyanAccount.withdraw(1000)    
waqasAccount.withdraw(1000)    