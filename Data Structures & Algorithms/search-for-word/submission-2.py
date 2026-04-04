class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m , n = len(board), len(board[0])

        def isValid(r,c):
            return 0<=r<m and 0<=c<n
        
        directions = [[0,-1], [0,1], [1,0],[-1,0]]
        visited = set()

        def dfs(r,c, pos):
            if board[r][c] != word[pos]:
                return False
            if pos == len(word)-1:
                return True
            for dx, dy in directions:
                nr, nc = r+dx, c+dy
                if (nr,nc) not in visited and isValid(nr,nc):
                    visited.add((nr,nc))
                    if(dfs(nr,nc, pos+1)):
                        return True
                    visited.remove((nr,nc))
            return False


        for i in range(m):
            for j in range(n):
                visited.add((i,j))
                if dfs(i,j,0):
                    return True
                visited.remove((i,j))
        
        return False
        