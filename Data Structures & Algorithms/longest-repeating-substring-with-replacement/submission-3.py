from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        L = 0
        ans = 0

        for R in range(len(s)):
            counter[s[R]] += 1
            while (R-L+1 - max(counter.values()) > k):
                counter[s[L]] -= 1
                L += 1
            
            ans = max(ans, R-L+1)
        
        return ans
        