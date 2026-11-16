from collections import defaultdict
from heapq import *
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        minHeap = []
        for u,v,w in edges:
            graph[u].append([w,v])
            graph[v].append([w,u])
        
        for weight, neighbor in graph[0]:
            heappush(minHeap,(weight, neighbor))


        edge_weight = 0
        visited = set()
        visited.add(0)

        while minHeap and len(visited) < n:
            weight, node = heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            edge_weight += weight

            for wt, neighbor in graph[node]:
                if neighbor not in visited:
                    heappush(minHeap, (wt, neighbor))

        return edge_weight if len(visited) == n else -1      