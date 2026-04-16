class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def expand(l,r):
            temp = 0
            while l >= 0 and r < n and s[l] == s[r]:
                temp += 1
                l -= 1
                r += 1
            return temp

        for i in range(n):
            ans += expand(i,i)
            ans += expand(i, i+1)
        
        return ans

        
        