from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while heap:
            print(heap)
            if len(heap) == 1:
                return -heap[0]
            first, second = -heappop(heap), -heappop(heap)

            if first != second:
                heappush(heap, -abs(first-second))

        return 0