stack=[]
data=[]
def login(name):
    fileData=open(name,"r")
    userdata=fileData.read()
    userdata=userdata.split()
    names=["ali","khan","noman","azam"]
    for  i in names:
        stack.append(i)
    # data=userdata
    # print(userdata)

login("ali")    
print(stack)


# print(names)
# print(stack)