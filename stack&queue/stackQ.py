class MyStack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def isEmpty(self):
        if self.length == 0:
            return True
        return False
    
    def push(self, x):
        self.stack.append(x)
        self.length += 1
    
    def popl(self):
        item = self.stack.pop()
        self.length -= 1
        return item
    
    def Top(self):
        return(self.stack[0])

    def stacksize(self):
        return self.length
    
    def print(self):
        print(self.stack)

class queue:
    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()

    def enqueue(self,x):
        if self.s1.stacksize == 0:
            self.s1.push(x)
        else:
            while not self.s1.isEmpty():
                self.s2.push(self.s1.popl())
            self.s1.push(x)

            while not self.s2.isEmpty():
                self.s1.push(self.s2.popl())
        # return self.s1

    def dequeue(self):
        return self.s1.popl()

    def peek(self):
        return self.s1.Top()

    def empty(self):
        return self.s1.isEmpty()

    def print(self):
        self.s1.print()
        # return self.s1
        # return "["+",".join(self.s1)+"]"



s = queue()
s.enqueue(7)
s.enqueue(5)
s.print()
print(s.peek())
s.enqueue(3)
s.print()
print(s.empty())
print(s.dequeue())
s.print()