class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] stores the number of ways to decode s[:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1 # Empty string has 1 way to be "decoded"
        dp[1] = 1 # We already checked s[0] != '0'
        
        for i in range(2, n + 1):
            # Check single digit (s[i-1])
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Check two digits (s[i-2:i])
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]
        