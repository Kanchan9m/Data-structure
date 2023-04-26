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
            
    def end(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def del_end(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            while temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = None
            print('Deleted data ',temp.data)
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
dl.end(8)
dl.end(10)
dl.printl()
dl.del_end()