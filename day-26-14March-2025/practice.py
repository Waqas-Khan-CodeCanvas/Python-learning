# list=[1,2,5,7,9,3,5,6]
list=[1,2,3,4,5,6,7,8,9]
print(list)
# for i in range(1,len(list)):
#     j=i
#     while list[j-1] > list[j] and j > 0:
#         list[j-1], list[j]=list[j], list[j-1]
#         j-=1
        
# print(list)    

# for i in range(len(list)-1,0,-1):
#     for j in range(i):
#         if list[j] > list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list) 
def search():
    n=5
    lower=0
    upper=len(list)-1

    while lower <= upper:
        mid = (lower+upper) //2 
        if list[mid] == n:
            print("found at ",mid)
            return True
            
        else:
            if list[mid] < n :
                lower = mid
            else:
                upper=mid    
               
search()
               