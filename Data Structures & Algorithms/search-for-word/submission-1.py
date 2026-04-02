class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        visited = set()

        def isValid(r, c):
            return 0<=r<m and 0<=c<n
        
        def backtrack(r,c,pos):
            if pos == len(word)-1 and board[r][c] == word[-1]:
                return True
            if board[r][c] == word[pos]:
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if isValid(nr,nc) and (nr,nc) not in visited :
                        visited.add((nr,nc))
                        if(backtrack(nr,nc, pos+1)):
                            return True
                        visited.remove((nr,nc))
            return False

                

        for i in range(m):
            for j in range(n):
                visited.add((i,j))
                if(backtrack(i,j,0)):
                    return True
                visited.remove((i,j))
        
        return False
        