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

    def position(self,data,pos):
        newnode = Node(data)
        if pos<1:
            print('greater than 1')
        elif(pos == 1):
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        else:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.next
            if temp != None:
                newnode.next = temp.next
                temp.next.prev = newnode
                temp.next = newnode
                newnode.prev = temp
            else:
                print('Poistion not exist')

    def del_pos(self,pos):
        if pos< 1:
            print('position should be greater than 1')
        elif pos == 1:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            print('deleted data ',temp.data)
            temp = None
        else:
            temp = self.head
            for i in range(1,pos):
                if temp != None:
                    curr = temp 
                    temp = temp.next
            if temp != None:
                curr.next = temp.next
                temp.next.prev = curr
                print('Deleted data ',temp.data)
                temp = None
            else:
                print('invalid position')
    
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
dl.position(12,2)
dl.printl()
dl.del_pos(2)