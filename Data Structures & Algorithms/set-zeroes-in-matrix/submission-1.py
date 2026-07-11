class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #using sets
        m, n = len(matrix), len(matrix[0])
        zero_rows , zero_cls = set(), set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                   zero_rows.add(r)
                   zero_cls.add(c)
        
        for r in range(m):
            for c in range(n):
                if r in zero_rows or c in zero_cls:
                    matrix[r][c] = 0
                    
        
        