class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def isPalindrome(c1, c2):
            while c1 >=0 and c2 < n and s[c1] == s[c2]:
                c1 -= 1
                c2 += 1
            return c1+1, c2-1
        
        l_max, r_max = 0, 0
        for i in range(n):
            max_l_odd, max_r_odd = isPalindrome(i,i)

            if (max_r_odd-max_l_odd+1) >= (r_max-l_max+1):
                l_max = max_l_odd
                r_max = max_r_odd
            
            max_l_even, max_r_even = isPalindrome(i,i+1)

            if (max_r_even-max_l_even+1) >= (r_max-l_max+1):
                l_max = max_l_even
                r_max = max_r_even

        return s[l_max:r_max+1]

        