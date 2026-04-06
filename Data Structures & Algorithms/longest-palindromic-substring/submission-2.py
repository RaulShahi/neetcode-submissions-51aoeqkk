from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxm = 0
        self.ans = ""
        n = len(s)
        @lru_cache
        def isPalindrome(i,j):
            l = i
            r = j
            while l < r:
                print("i","j","l","r",i,j,l,r)
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        @lru_cache
        def dp(i,j):
            if i > j or i < 0 or j >= n:
                return
            if isPalindrome(i,j):
                if j-i+1 > self.maxm:
                    self.maxm = j-i+1
                    self.ans = s[i:j+1]

                return
            
            dp(i+1,j)
            dp(i,j-1)
        
        dp(0, n-1)
        return self.ans

        