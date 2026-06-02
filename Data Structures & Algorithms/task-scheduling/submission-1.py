from collections import deque, Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)

        maxHeap = [-val for val in count.values()]
        heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
            
        return time
            

        