class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open, closed):
            if len(curr) == 2*n:
                res.append("".join(curr[:]))
            
            if open < n:
                curr.append("(")
                backtrack(curr, open+1, closed)
                curr.pop()
            
            if closed < open:
                curr.append(")")
                backtrack(curr, open, closed+1)
                curr.pop()
        
        backtrack([], 0, 0)
        return res
        