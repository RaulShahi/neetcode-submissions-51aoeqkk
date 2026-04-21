from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dp(i, holding):
            if i >= len(prices):
                return 0
            
            if holding:
                return max(prices[i] + dp(i+2, 0), dp(i+1, 1))
            
            else:
                return max(-prices[i] + dp(i+1, 1), dp(i+1, 0))

        return dp(0, 0)
        