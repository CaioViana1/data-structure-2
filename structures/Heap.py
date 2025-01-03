from heapq import *
from structures.Registro import Registro

class Heap:
    def __init__(self):
        self.heap:list[Registro] = []
    
    def push(self, item):
        heappush(self.heap, item)
    
    def pop(self):
        return heappop(self.heap)
    
    def first(self):
        try:
            return self.heap[0]
        except:
            return None
    
    def isEmpty(self):
        return (len(self.heap) < 1) 
    
    def __len__(self):
        return len(self.heap)
    
    def __getitem__(self, index):
        return self.heap[index]
    
    def __str__(self):
        return str(self.heap)  
    
    def unflagAll(self):
        for r in self.heap:
            r.delFlag()

    def flagAll(self):
        for r in self.heap:
            r.setFlag()

        