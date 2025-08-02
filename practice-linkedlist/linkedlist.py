class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
node1=Node(10)
node2=Node(11)
node3=Node(12)
node4=Node(13)

class Linkedlist:
    def __init__(self):
        self.head=None
    def printLinkedlist(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, n.ref,end=" -> " )
                n =n.ref    
        
list=Linkedlist()
list.head =node1

list.head.ref=node2
node2.ref=node3
node3.ref=node4
# print(list.head.data)
# print(node2)
# print(list.head.ref.data)
list.printLinkedlist()


