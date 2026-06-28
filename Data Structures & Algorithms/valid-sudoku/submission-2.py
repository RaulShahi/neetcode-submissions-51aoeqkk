from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                
                if val in rows[i] or val in columns[j] or val in squares[(i//3, j//3)]:
                    return False
                
                rows[i].add(val)
                columns[j].add(val)
                squares[(i//3,j//3)].add(val)
        
        return True
        