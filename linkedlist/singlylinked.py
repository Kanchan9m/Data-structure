class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def addbeg(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def addend(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode

    def position(self,data,pos):
        newnode = Node(data)
        if pos <1:
            print('pos should be greater then 1')
        elif pos==1:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            for i in range(1,pos-1):
                if temp != None:
                    temp = temp.next
            if temp != None:
                newnode.next = temp.next
                temp.next = newnode
            else:
                print('position not valid')

    # def del_beg(self):
    #     if self.head == None:
    #         return None
    #     else:
    #         temp = self.head
    #         self.head = temp.next
    #         print('Deleted data ',temp.data)
    #         temp = None

    # def del_end(self):
    #     if self.head == None:
    #         return None
    #     else:
    #         temp = self.head
    #         while temp.next != None:
    #             prev = temp
    #             temp = temp.next
    #         prev.next = None
    #         print('Deleted data ',temp.data)
    #         temp = None

    # def delposition(self,pos):
    #     if pos < 1:
    #         print('position note valid')
    #     elif pos == 1:
    #         temp = self.head
    #         self.head = temp.next
    #         print('Deleted data ',temp.data)
    #         temp = None
    #     else:
    #         temp = self.head
    #         for i in range(1,pos):
    #             prev = temp 
    #             temp = temp.next
    #         if temp!= None:
    #             prev.next = temp.next 
    #             print(temp.data)
    #             temp = None
    #         else:
    #             print('invalid position')

    def println(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            print('data')
            while temp!= None:
                print(temp.data,end = ' ')
                temp = temp.next

ll = Linkedlist()
ll.addbeg(5)
ll.addbeg(6)
ll.println()
ll.addend(8)
ll.println()
ll.position(10,2)
ll.position(11,6)
ll.println()
# ll.del_beg()
# ll.del_end()
# ll.delposition(1)