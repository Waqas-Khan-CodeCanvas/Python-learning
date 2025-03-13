data={
    "user1": {'name': 'ali','age': 30,'city': 'New York'},
    "user2": {'name': 'hamza','age': 30,'city': 'New York'},
    "user3": {'name': 'sufyan','age': 30,'city': 'New York'},
    "user4": {'name': 'waqas','age': 30,'city': 'New York'},
    "user5": {'name': 'zaryab','age': 30,'city': 'New York'},
    "user6": {'name': 'khan','age': 30,'city': 'New York'},
}

print(data)
print(data['user1'])
print(data['user1']["name"])

for users in data:
    # print(data[users])
    # print(data[users]["name"])
    for key ,value in data[users].items():
        print(F"your {key} is {value}")
    print("\n")    