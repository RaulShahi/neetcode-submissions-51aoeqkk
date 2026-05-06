from heapq import *
from math import *
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False
        
        if self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        
        elif self.rank[rootY] < self.rank[rootX]:
            self.root[rootY] = rootX
        
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        tree = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2,y2 = points[j]
                cost = abs(x2-x1) + abs(y2- y1)
                edge = Edge(i,j,cost)
                tree.append(edge)
        
        heapify(tree)

        result = 0
        count = n-1

        while tree and count > 0:
            edge = heappop(tree)
            if uf.union(edge.point1, edge.point2):
                result += edge.cost
                count -= 1
        
        return result
                    
                
        