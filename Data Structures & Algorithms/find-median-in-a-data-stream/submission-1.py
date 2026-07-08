from heapq import *
class MedianFinder:

    def __init__(self):
        #two heaps, large, small, minheap, maxheap
        self.small , self.large = [], []

    def addNum(self, num: int) -> None:
        #always push to the small(maxheap)
        heappush(self.small, (-1*num))

        #make sure every element in small <= every element in large heap
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            el = (-1*heappop(self.small))
            heappush(self.large, el)
        
        #uneven size greater than 1
        if len(self.small) > len(self.large)+1:
            el = (-1*heappop(self.small))
            heappush(self.large, el)
        
        if len(self.large) > len(self.small) + 1:
            el = heappop(self.large)
            heappush(self.small, -1*el)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return ((-1*self.small[0])+self.large[0])/2
        
        