class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0

        L = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            ans = max(ans, R-L+1)
            window.add(s[R])
        
        return ans

        