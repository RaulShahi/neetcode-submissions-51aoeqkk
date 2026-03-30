from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            first, second = -heappop(heap), -heappop(heap)

            if first != second:
                heappush(heap, -(first- second))
        
        return 0 if len(heap) == 0 else -heap[0]

        