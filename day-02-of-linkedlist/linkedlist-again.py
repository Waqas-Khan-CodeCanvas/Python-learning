
class Node:
    def __init__(self, data):
      self.data = data
      self.ref = None
      
class Linkedlist:
    def __init__(self):
      self.head = None
      
    def printlist(self):
        if self.head is None:
            print("your Linked list is empty") 
        else:
            n = self.head
            while n is not None:
                print(n.data , end=" -> ") 
                n = n.ref 
    
    def add_begin(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head =new_node
        else:    
            new_node.ref = self.head
            self.head = new_node
            print("added at begin")  
    
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
            
# creating nodes 
node1 = Node(10)  
node2 = Node(11)  
node3 = Node(12) 

# linking the node to each other
list = Linkedlist()
list.head = node1
node1.ref = node2
node2.ref = node3

list.add_begin(9)
list.add_end(14)
list.add_between(11,20)
list.printlist()


# list = [ 1,2,3,4,5,6,7]
# list.append(10)
# print(list)



