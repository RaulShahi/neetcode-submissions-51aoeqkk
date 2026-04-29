class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.components = size
    
    # [0,1,2,3,4]
    def find(self, x):
        #O(alpha N)-almost constant
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        #O(alpha N)-almost constant

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            #cycle detected
            return False

   
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        self.components -= 1
        return True

    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for x, y in edges:
            #O(E)
            if(not uf.union(x,y)):
                return False
        
        return uf.components == 1

#Time - O(n) (for constructor) + O(E . alphaN) = O(n)
#Space - O(n)
        