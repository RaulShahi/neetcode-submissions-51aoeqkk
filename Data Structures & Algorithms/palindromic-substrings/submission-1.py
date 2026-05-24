class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        def palindrome(c1, c2):
            ans = 0
            while c1 >= 0 and c2 < n and s[c1] == s[c2]:
                ans += 1
                c1 -= 1
                c2 += 1
            
            return ans
        
        for i in range(n):
            res += palindrome(i,i)
            res += palindrome(i, i+1)
        
        return res

        