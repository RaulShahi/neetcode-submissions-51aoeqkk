class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        resLen = 0

        for i in range(n):
            #odd length
            l,r =i,i

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            if (r-1)-(l+1)+1 > resLen:
                res = s[l+1:r]
                resLen = (r-1) -(l+1) + 1
            
            #even length
            l,r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            if (r-1)-(l+1)+1 > resLen:
                res = s[l+1:r]
                resLen = (r-1) -(l+1) + 1

        
        return res