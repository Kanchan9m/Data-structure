#Stack using Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Mystack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1
    
    def pop(self):
        if self.head == None:
            return -1
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp.data

    def top(self):
        return self.head.data

    def sizeo(self):
        return self.length

    def empty(self):
        if self.head == None:
            return True
        return False

# class Mystack:

#     def __init__(self):
#         self.s1 = Linkedlist()

#     def push(self,x):
#         self.s1.insertion(x)

#     def pop(self):
#         return self.s1.deletion()

#     def top(self):
#         return self.s1.peek()
    
#     def sizeo(self):
#         return self.s1.size()

#     def empty(self):
#         return self.s1.isEmpty()

s = Mystack()
s.push(5)
s.push(6)
s.push(9)
print(s.empty())
print(s.sizeo())
print('peek')
print(s.top())
print('deleted')
print(s.pop())
print('peek')
print(s.top())
print(s.sizeo())
print(s.empty())