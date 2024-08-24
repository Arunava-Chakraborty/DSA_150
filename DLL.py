class Node:
    def __init__(self , data):
        self.data = data
        self.pref = None
        self.nref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.nref
            print("\n")

    def print_LL_reverse(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.pref
    def insertion(self ,x):
        if self.head is None:
            new_node = Node(10)
            self.head = new_node
        else:
            print('Linked list is empty')
    def add_begin(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.nref = n
            n.pref = new_node
            self.head = new_node

    def add_end(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def insert_after(self, data,x):
        new_node = Node(data)
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            new_node.pref = n.nref.pref
            new_node.nref = n.nref
            n.nref = new_node
            new_node.nref.pref = new_node
    def insert_befor(self , data ,x):
        new_node = Node(data)
        if self.head is None:
            print("The LL is empty")

        if self.head.nref == None:
            self.add_begin(data)

        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given postion is not avialable")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node


dll1 = DoublyLL()
dll1.add_begin(10)
dll1.add_end(20)
dll1.add_begin(30)
dll1.add_end(40)
dll1.insert_after(50, 20)
dll1.insert_after(60, 20)
dll1.insert_after(70, 20)
dll1.insert_befor(80,20)
dll1.insert_befor(90,20)
dll1.print_LL()
dll1.print_LL_reverse()
class Node:
    def __init__(self , data):
        self.data = data
        self.pref = None
        self.nref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.nref
            print("\n")

    def print_LL_reverse(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.pref
    def insertion(self ,x):
        if self.head is None:
            new_node = Node(10)
            self.head = new_node
        else:
            print('Linked list is empty')
    def add_begin(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.nref = n
            n.pref = new_node
            self.head = new_node

    def add_end(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def insert_after(self, data,x):
        new_node = Node(data)
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            new_node.pref = n.nref.pref
            new_node.nref = n.nref
            n.nref = new_node
            new_node.nref.pref = new_node
    def insert_befor(self , data ,x):
        new_node = Node(data)
        if self.head is None:
            print("The LL is empty")

        if self.head.nref == None:
            self.add_begin(data)

        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given postion is not avialable")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node


dll1 = DoublyLL()
dll1.add_begin(10)
dll1.add_end(20)
dll1.add_begin(30)
dll1.add_end(40)
dll1.insert_after(50, 20)
dll1.insert_after(60, 20)
dll1.insert_after(70, 20)
dll1.insert_befor(80,20)
dll1.insert_befor(90,20)
dll1.print_LL()
dll1.print_LL_reverse()
