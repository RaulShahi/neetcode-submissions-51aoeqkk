from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        L = 0
        ans = 0

        for R in range(len(s)):
            count[s[R]] += 1
            while (R-L+1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
                
            ans = max(ans, R-L+1)
        return ans
        