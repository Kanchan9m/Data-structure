#stack using list

stack = []
stack.append(5)
stack.append(7)
stack.append(9)
stack.append(2)
stack.append(10)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

#stack using linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            # top = self.head

    def pop(self):
        if self.head == None:
            print('stack is empty')
        else:
            temp = self.head
            self.head = temp.next
            print('pop element ',temp.data)
            temp = None
    
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

s = Stack()
s.push(5)
s.push(7)
s.display()
s.pop()
        
