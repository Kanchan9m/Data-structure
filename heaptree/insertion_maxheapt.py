# Heap tree with the use of Array

class Maxheap:
    
    def __init__(self):
        self.heap = []

    def insert(self,value):
        self.heap.append(value)
        self._heapifyup(len(self.heap)-1)

    def is_empty(self):
        return len(self.heap) == 0
    
    def _heapifyup(self,index):

        # return parent node index
        p = (index -1)//2

        if index > 0 and self.heap[index] > self.heap[p]:

            # swap parent node with given node
            self.heap[index], self.heap[p] = self.heap[p], self.heap[index]
            self._heapifyup(p)

            # index = p
    
heap = Maxheap()
heap.insert(20)
heap.insert(11)
heap.insert(15)
heap.insert(10)
heap.insert(8)
heap.insert(12)
heap.insert(22)

print(heap.heap)