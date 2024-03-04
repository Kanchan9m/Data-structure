class Queue:
    def __init__(self):
        self.queue = []
        # self.front = 0
        self.length = 0

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def enqueue(self,x):
        self.queue.append(x)
        self.length += 1

    def dequeue(self):
        item = self.queue.pop(0)
        # self.front += 1
        return item
    
    def qsize(self):
        return self.length

    def print(self):
        print(self.queue)

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,x):
        self.q2.enqueue(x)

        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.dequeue()
    
    def print(self):
        self.q1.print()

s = MyStack()
s.push(4)
s.push(5)
s.print()
print(s.pop())