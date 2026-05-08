#Applying Dikstra's algorithm
from heapq import *
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float("inf")] * (n+1)
        graph = defaultdict(list)

        for x,y,cost in times:
            graph[x].append([y,cost])
        
        distances[k] = 0

        heap = [(0, k)]

        while heap:
            cur_dist , node = heappop(heap)

            if cur_dist > distances[node]:
                continue
            
            for nei, cost in graph[node]:
                dist = cur_dist + cost
                if dist < distances[nei]:
                    distances[nei] = dist
                    heappush(heap, (dist, nei))
        
        ans = max(distances[1:])
        return ans if ans != float("inf") else -1
            


