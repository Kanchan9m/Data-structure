
 class Queue:
     queue = []
     def inqueue(self, ele):
         self.queue.append(ele)
        
    def size(self):
        return len(self.queue)
    
    def peek(self):
        b = self.queue(0)
        return b
    
    def dequeue(self):
        if not self.queue:
            print('Queue is empty')
            return None
        else:
            a = self.queue.pop(0)
            return a
    def printQueue(self):
        for i in self.queue:
            print(i,end = ' ')
            
print("Queue start")       
q = Queue()
q.inqueue(6)
q.inqueue(7)
q.inqueue(45)

print('size ',q.size())
print('removed ele ',q.dequeue())
q.printQueue()
