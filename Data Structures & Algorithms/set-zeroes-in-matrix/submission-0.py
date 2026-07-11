class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Brute force approach
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for row in range(m):
                        if matrix[row][c] != 0:
                            matrix[row][c] = None
                    
                    for cl in range(n):
                        if matrix[r][cl] != 0:
                            matrix[r][cl] = None
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == None:
                    matrix[r][c] = 0
    

        
        