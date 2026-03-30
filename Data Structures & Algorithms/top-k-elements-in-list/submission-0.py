from collections import defaultdict, Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        heapify(heap)

        for key,freq in count.items():
            heappush(heap, (freq, key))
            if len(heap) > k:
                heappop(heap)
        
        return [b for (a,b) in heap ]


        