class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None   # head is a reference to the first node
        
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref = self.head
        self.head = new_node  
    def add_end(self,data):
        new_node = Node(data)
        if self.head is Node:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n=n.ref
            n.ref =new_node
            print( "inserted at the end")
                          
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->")
                n = n.ref    

list1 = LinkedList()
list1.print_LL()
list1.head = Node(10)
secondnode=Node(20)
thirdnode=Node(30)
list1.add_begin(1)

list1.head.ref = secondnode
secondnode.ref = thirdnode

list1.add_end(50)
list1.print_LL()

print(list1)
