#Prim's algorithm
from heapq import *
class Edge(object):
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        count = size - 1
        result = 0
        visited = [False] * size


        x1, y1 = points[0]
        pq = []

        for j in range(1, size):
            x2, y2 = points[j]
            cost = abs(x1-x2) + abs(y1-y2)
            edge = Edge(0, j, cost)
            heappush(pq, edge)
            
        visited[0] = True
        while pq and count > 0:
            edge = heappop(pq)
            cost = edge.cost
            point1= edge.point1
            point2= edge.point2

            #cycle detection
            if not visited[point2]:
                result += cost
                visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0]-points[j][0]) + abs(points[point2][1]-points[j][1])
                        heappush(pq, Edge(point2, j, distance))
                count -= 1
        return result

        
        

        
        