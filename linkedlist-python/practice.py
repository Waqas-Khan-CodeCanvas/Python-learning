class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
      
class Linkedlist:
    def __init__(self):
        self.head = None  
        
    def printItems(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data , end=" -> ")
                n = n.ref    
                
    def add_begin(self,item):
        new_node=Node(item) 
        if self.head is None:
            self.head = new_node
        else:
            n = self.head    
            new_node.ref = n
            self.head = new_node
            print("add at begin") 
    
    def add_end(self,item):
            new_node = Node(item)
            if self.head is None:
                self.head = new_node
            else:
                n = self.head
                while n.ref is not None: 
                    n = n.ref
                n.ref = new_node  
                print("added at end")
    def add_between(self,position,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if n.data == position:
                    new_node.ref = n.ref
                    n.ref = new_node
                    print("added in between")                 
                    break
                n =n.ref
# creating nodes for linkedlist      
node1 = Node(10)          
node2 = Node(12)          
node3 = Node(13)    

# connecting and chaining nodes to each other
list=Linkedlist()
list.head=node1
node1.ref = node2
node2.ref = node3

# print elements
list.add_begin(9)
list.add_end(30)
list.add_between(12,22)
list.printItems()




