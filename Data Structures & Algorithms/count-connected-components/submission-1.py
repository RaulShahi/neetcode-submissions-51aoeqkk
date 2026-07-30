class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.connected = size
    
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
            
            self.connected -= 1
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x,y in edges:
            uf.union(x,y)
        
        return uf.connected
        