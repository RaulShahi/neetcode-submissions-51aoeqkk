from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.maxm = 0
        self.ans = ""

        @lru_cache(None)
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        @lru_cache(None)
        def dp(i, j):
            if i > j or i < 0 or j >= n:
                return

            if isPalindrome(i, j):
                if j - i + 1 > self.maxm:
                    self.maxm = j - i + 1
                    self.ans = s[i:j+1]
                return

            dp(i + 1, j)
            dp(i, j - 1)

        dp(0, n - 1)
        return self.ans