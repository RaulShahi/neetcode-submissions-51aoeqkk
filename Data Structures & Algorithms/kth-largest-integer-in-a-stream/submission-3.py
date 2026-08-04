from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > k:
                heappop(self.heap)
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        
        return self.heap[0]
