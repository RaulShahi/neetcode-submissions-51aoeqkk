from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for n,v in count.items():
            heappush(heap, (v,n))
            while len(heap) >k:
                heappop(heap)
        return [val[1] for val in heap]

        