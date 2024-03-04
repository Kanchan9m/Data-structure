class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def isEmpty(self):
        if self.front  == None:
            return True
        return False
        
    def push(self, item): 
        newnode = Node(item)
        if self.rear == None:
            self.front = newnode
            self.rear = newnode
    
        else:
            self.rear.next = newnode
            self.rear = newnode
        self.length += 1
        
    def sizeo(self):
        print("size ",self.length)
        
    def pop(self):
        if self.isEmpty():
            return 
        else:
            temp = self.front
            self.front = temp.next
            self.length -= 1
            return temp.data
    
s = queue()
s.push(6)
s.push(3)
s.push(4)
s.push(5)
s.sizeo()
print(s.pop())
s.sizeo()
print(s.pop())