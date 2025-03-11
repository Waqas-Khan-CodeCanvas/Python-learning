row=8
# for i in range(1,row+1):
#     print("* " * i)
     
# for i in range(row+1,0,-1):
#     print("* " * i)
 

for i in range(1,row+1):
    print(" "*(row-i)+"* "*i)

for i in range(row + 1,0,-1):
    print(" " * (row - i) + "* " * i)    