class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        # Finds the root of x
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            self.num_components -= 1
            return True
        return False

    def getNumComponents(self) -> int:
        return self.num_components

