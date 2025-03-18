# # position=0
# # def search(list,n):
# #     lower=0
# #     upper=len(list)-1
# #     while lower <= upper:
# #         mid=(lower+upper) // 2
# #         if list[mid]==n:
# #             globals() ['position'] =mid
# #             return True
# #         else:
# #             if list[mid] < n:
# #                 lower=mid
# #             else:
# #                 upper=mid    
    
# # list =[1,2,4,5,6,7,8,9]
# # n=2
# # # search(list,n)
# # # print(list)
# # if search(list,n):
# #     print("found at ", position)
# # else:
# #     print("not found")    

# # list = [1, 2, 4, 5, 6, 7, 8, 9]
# # n = 2

# # lower = 0
# # upper = len(list) - 1
# # found = False

# # while lower <= upper:
# #     mid = (lower + upper) // 2
# #     if list[mid] == n:
# #         print("Found at index", mid)
# #         found = True
# #         break
# #     elif list[mid] < n:
# #         lower = mid + 1  # Move to the right half
# #     else:
# #         upper = mid - 1  # Move to the left half

# # if not found:
# #     print("Not found")

# list=[1,2,3,4,5,6,7,8,9,10]
# userinput=int(input("enter a number you want to find from list :"))
# lower=1
# upper=(len(list)-1)
# found=False

# while lower <= upper:
#     mid=(lower+upper)//2
#     if list[mid]==userinput:
#         print("found at index " ,mid )
#         found =True
#         break
#     else:
#         if list[mid]<userinput:
#            lower=mid
#         else:
#             upper=mid 
# if found:
#     print("item found")
# else:
#     print("item is not found")

num = [8, 4, 5, 2, 9,2,1]
for i in range(1, len(num)):
        j = i 
        while j >= 0 and j > 0:
            num[j],num[j - 1] = num[j-1],num[j]
            j -= 1
            

print("Sorted Array:", num)
