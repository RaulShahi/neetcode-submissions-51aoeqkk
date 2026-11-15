from heapq import *
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        distances = {}
        for i in range(n):
            distances[i] = float("infinity") 
        distances[src] = 0
        minHeap = [(0, src)]

        graph = defaultdict(list)

        for u,v,w in edges:
            graph[u].append([w,v])

        while minHeap:
            cur_dist, node = heappop(minHeap)

            if cur_dist > distances[node]:
                continue
            
            for weight, neighbor in graph[node]:
                dist = cur_dist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heappush(minHeap, (dist, neighbor))
        
        for node, dist in distances.items():
            if dist == float("inf"):
                distances[node] = -1
        
        return distances
    
    #Time Complexity => ElogV. V vertices, so edges can be V square. 
    #Space Complexity => O(V) to store all the vertices 
        