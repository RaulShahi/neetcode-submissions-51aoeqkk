class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        board_count = Counter()

        for i in range(m):
            for j in range(n):
                board_count[board[i][j]] += 1
        
        word_count =  Counter(word)

        for ch in word:
            if word_count[ch] > board_count[ch]:
                return False


        def isValid(r,c):
            return 0<=r<m and 0<=c<n
        
        visited = set()
        res = []

        def dfs(r,c,pos):
            if board[r][c] != word[pos]:
                return False
            
            if pos == len(word)-1:
                return True
            
            for dx, dy in directions:
                nr, nc = r+dx, c+dy
                if isValid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    if(dfs(nr,nc, pos+1)):
                        return True
                    
                    visited.remove((nr,nc))
            return False
        
        for i in range(m):
            for j in range(n):
                visited.add((i,j))
                if(dfs(i,j,0)):
                    return True
                visited.remove((i,j))
        
        return False   