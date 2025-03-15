position=0
def search(list,n):
    lower=0
    upper=len(list)-1
    while lower <= upper:
        mid=(lower+upper) // 2
        if list[mid]==n:
            globals() ['position'] =mid
            return True
        else:
            if list[mid] < n:
                lower=mid
            else:
                upper=mid    
    
list =[1,2,4,5,6,7,8,9]
n=2
# search(list,n)
# print(list)
if search(list,n):
    print("found at ", position)
else:
    print("not found")    

