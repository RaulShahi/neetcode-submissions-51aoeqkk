from collections import defaultdict
from heapq import *

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

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
            elif self.rank[rootY] < self.rank[rootX]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        
        return False
            


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for u,v,w in edges:
            heappush(minHeap, (w,u,v))
        uf = UnionFind(n)
        res, components = 0, n

        while minHeap and components > 1:
            weight, n1, n2 = heappop(minHeap)

            if uf.union(n1, n2):
                res += weight
                components -= 1
        
        return res if components == 1 else -1



