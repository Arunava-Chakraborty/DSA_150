class Node:
    def __init__(self , data):
        self.data = data
        self.ref = None
    # This will create a node and just the node only and the reference value will be none then we create a class for linking the nodes.

class LinkedList:
  
    def __init__(self):
        self.head = None
        self.temp = None
      
    def print_LL(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
              
    def add_begin(self , data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head =new_node
      
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.ref is not None:
                temp= temp.ref
            temp.ref = new_node
          
    def insert_after(self, data,x):
        n=self.head
        while n is not None:
            if x == n.data:
                break
            n= n.ref
        if n is None:
            print("Position not avialable")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
          
    def insert_before(self, data, x):
        if self.head == None:
            print("Linked List is null!")
            return
        if self.head.data ==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data ==x:
                    break
                n =  n.ref
            if n.ref == None:
                print("Node is not found")
            else:
                new_node=Node(data)
                new_node.ref = n.ref
                n.ref =new_node


#Test Cases
ll1 = LinkedList()
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(40)
ll1.add_end(50)
ll1.add_end(60)
ll1.insert_after(10 ,20)
ll1.insert_before(80 , 10)
ll1.print_LL()



