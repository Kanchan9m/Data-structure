# insertion and deletion in min heap 
# heapify heap tree in both up heapify and down heapify

class Minheap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def delete(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        
        root = self.heap[0]
        last_element = self.heap.pop()
        
        if not self.is_empty():
            self.heap[0] = last_element
            self._heapify_down(0)
        
        return root
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def _heapify_up(self, index):
        p = (index - 1) // 2
        
        if index > 0 and self.heap[index] < self.heap[p]:
            self.heap[index], self.heap[p] = self.heap[p], self.heap[index]
            self._heapify_up(p)
    
    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Example usage
heap = Minheap()
heap.insert(20)
heap.insert(11)
heap.insert(15)
heap.insert(10)
heap.insert(8)
heap.insert(12)
heap.insert(22)

print(heap.heap)
print(heap.delete())
print(heap.heap)