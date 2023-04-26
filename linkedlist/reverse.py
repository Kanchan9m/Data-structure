class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
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
    def reverse(self):
        if self.head == None:
            print('List is empty')
        elif self.head.next == None:
            print('only one element')
        else:
            temp1 = self.head
            temp2 = temp1.next
            temp3 = temp2.next
            temp1.next = None
            while temp3 != None:
                temp2.next = temp1
                temp1 = temp2
                temp2 = temp3
                temp3 = temp3.next
            temp2.next = temp1
            self.head = temp2

    def println(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while temp!= None:
                print(temp.data)
                temp = temp.next


ll = linkedlist()
ll.create(5)
ll.create(6)
ll.create(8)
ll.create(10)
ll.create(9)
ll.println()
ll.reverse()
ll.println()