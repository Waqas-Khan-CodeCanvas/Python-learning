# def bubbleSort(num):
#     for i in range(len(num)-1,0,-1):
#         for j in range(i):
#             if num[j] > num[j+1]:
#                 temp=num[j]
#                 num[j]=num[j+1]
#                 num[j+1]=temp
                
# num=[1,5,3,7,9,5,2,4,6,8]
# bubbleSort(num)
# print(num)

num=[1,5,3,7,9,5,2,4,6,8]
for i in range(len(num)-1,0,-1):
     for j in range(i):
        if num[j] > num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp  
                
print(num)

# https://pythontutor.com/javascript.html#mode=edit
# https://sortvisualizer.com/insertionsort/