class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        max_len = 0
        for i in range(len(s)):
            #odd length

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    left, right = l, r
                    max_len = r-l+1
                r += 1
                l -= 1
            
            #even length
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    left, right = l, r
                    max_len = r - l +1
                r += 1
                l -= 1
        
        return s[left:right+1]

        