import random
def Printarray(ArrayData):
    for x in range(0, 10):
        for y in range(0, 10):
            print(ArrayData[x][y], " ", end='')
            print("")
# main
# list =list(range(1,1000))
ArrayData= [[0]*10 for i in range(10)] #integer
print(ArrayData)
for x in range(0, 10):
    for y in range(0,10):
        ArrayData[x][y] = random.randint(1, 100)
print(ArrayData)
print("")
for i in ArrayData:
    print(i)
# print("Before")
ArrayLength = 10
for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength):
        for Z in range(0, ArrayLength - Y - 1):
            if(ArrayData[X][Z] > ArrayData[X][Z+1]):
                ArrayData[X][Z],ArrayData[X][Z+1] = ArrayData[X][Z+1],ArrayData[X][Z]
print("After")
Printarray(ArrayData)