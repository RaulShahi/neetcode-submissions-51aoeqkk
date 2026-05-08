#Kruskal's Algorithm
from heapq import *
class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.root = [i for i in range(size)]
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def connected(self, x,y):
        return self.find(x) == self.find(y)

class Edge(object):
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        count = size - 1
        uf = UnionFind(size)
        pq = []

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i, size):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                edge = Edge(i, j, cost)
                pq.append(edge)
        
        heapify(pq)
        result = 0

        while pq and count > 0:
            edge = heappop(pq)
            if not uf.connected(edge.point1, edge.point2):
                result += edge.cost
                uf.union(edge.point1, edge.point2)
                count -= 1
        return result

        