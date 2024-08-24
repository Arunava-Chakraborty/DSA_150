class Node:
    def __init__(self , data):
        self.data = data
        self.ref = None
    # This will create a node and just the node only and the reference value will be none then we create a class for linking the nodes.

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data , "--->" , end=" ")
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

    def delete_beg(self):
        n= self.head
        if self.head is None:
            print("LL is Empty")
            return
        if n.ref is None:
            self.head = None
        else:
            self.head = n.ref.ref

    def deletion(self):
        n = self.head
        if self.head == None:
            print("Linked List is null!")
            return
        if n.ref == None:
            self.delete_beg()
        while n.ref is not None:
            if n.ref.ref ==None:
                n.ref =None
                break
            n = n.ref
    def delete_value(self , x):
        n = self.head
        if self.head == None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    n.ref = n.ref.ref
                    break
                n=n.ref
ll1 = LinkedList()
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(40)
ll1.add_end(50)
ll1.add_end(60)
ll1.delete_value(40)
ll1.delete_value(20)
ll1.delete_value(10)
ll1.delete_value(50)
ll1.delete_value(60)
ll1.add_end(40)
ll1.add_begin(70)

ll1.print_LL()



