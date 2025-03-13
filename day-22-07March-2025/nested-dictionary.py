# nested dictionary in python

data={
    "user1":{'name':'ali','age':23,'city':'karachi'},
    "user2":{'name':'ahmed','age':24,'city':'lahore'},
    "user3":{'name':'hamza','age':25,'city':'islamabad'},
    "user4":{'name':'sufyan','age':26,'city':'quetta'},
    "user5":{'name':'zaryab','age':27,'city':'peshawar'},
    "user6":{'name':'amna sufyan','age':28,'city':'multan'},
} 

# write a function to print all the users with their details
def printUserDetails(userData):
    for user in userData:
        for userKey, userValue in userData[user].items():
            print(f"{userKey} : {userValue}")
        print("\n")
    
printUserDetails(data)    