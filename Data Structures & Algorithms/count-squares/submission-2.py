from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pts = []
        self.ptsCount = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for px, py in self.pts:
            if (abs(px-x) != abs(py-y)) or px==x or py==y:
                continue
            res += self.ptsCount[(px,y)] * self.ptsCount[(x,py)]
        
        return res
        
