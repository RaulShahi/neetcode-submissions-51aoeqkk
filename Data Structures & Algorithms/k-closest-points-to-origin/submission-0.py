from math import *
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x,y):
            return sqrt(x**2+y**2)
        
        heap = []

        for x,y in points:
            dist = distance(x,y)
            heapq.heappush(heap, (-dist,[x,y]))

            if len(heap)>k:
                heappop(heap)
        
        return [val[1] for val in heap]
        

        