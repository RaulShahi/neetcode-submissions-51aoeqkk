from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el == ".":
                    continue
                if(el in rows[i] or
                    el in columns[j] or 
                    el in squares[(i//3,j//3)]):
                    return False
                rows[i].add(el)
                columns[j].add(el)
                squares[(i//3,j//3)].add(el)
        
        return True
        