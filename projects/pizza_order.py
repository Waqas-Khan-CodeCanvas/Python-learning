

name=input("    Enter you name here : ")
size=""
total_bill=0
order_number=50259028

if name!="":
    print("small pizza")
    print("meddium pizza")
    print("large pizza \n")
    size=input("    Enter your pizza size ")
else:
    print("invalid input ")  

chese=""
if size=="small":
    print("   small pizza price is : Rs:100")
    chese=input("   Do you want extra chese (y/n) \n ")
    total_bill += 100

    if chese=="y":
        print(" extra chese price is : Rs:10")
        total_bill+=10
    else:
        print(" okay thank you as you wish")

elif size=="medium":
    print(" medium pizza price is : Rs:200")
    chese=input("   Do you want extra chese (y/n)\n ")
    total_bill+=200

    if chese=="y":
        print(" extra chese price is : Rs:20")
        total_bill+=20
    else:
        print(" okay thank you as you wish")

elif size=="large":
    print(" large pizza price is : Rs:300")
    chese=input("   Do you want extra chese (y/n) ")
    total_bill+=300

    if chese=="y":
        print(" extra chese price is : Rs:30")
        total_bill+=30
    else:
        print(" okay thank you as you wish")
else:
    print(" invalid input for pizza")        

print(f"\n your name is : {name}")
print(f"your order number is : {order_number}")
print(f"your have ordered : {size} pizza")
print(f"your total bill is  : {total_bill}")
