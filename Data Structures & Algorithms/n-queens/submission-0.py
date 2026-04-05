class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        posdiag = set()
        negdiag = set()

        board = [["."] * n for i in range(n)]

        res = []

        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in columns or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                columns.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                columns.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res


