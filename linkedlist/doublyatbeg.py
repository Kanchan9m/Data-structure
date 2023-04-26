class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
class doubly:
    def __init__(self):
        self.head = None
    def create(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next 
            temp.next = newnode
            newnode.prev = temp
            
    def beg(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def del_beg(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            print('deleted data ',temp.data)
            temp = None

    def printl(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while (temp!= None):
                print(temp.data)
                temp = temp.next
dl = doubly()
dl.create(5)
dl.create(9)
dl.beg(7)
dl.printl()
dl.del_beg()