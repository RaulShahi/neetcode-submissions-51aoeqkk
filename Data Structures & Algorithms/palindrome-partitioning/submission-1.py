class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(l,r):
            while l <r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            return True

        def backtrack(curr,i):
            # current partition and current index
            if i>= len(s):
                res.append(curr[:])
            
            for j in range(i, len(s)):
                if isPalindrome(i,j):
                    curr.append(s[i:j+1])
                    backtrack(curr, j+1)
                    curr.pop()

        
        backtrack([],0)

        return res