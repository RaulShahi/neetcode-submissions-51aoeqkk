from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, remaining):
            if remaining == 0:
                return 1
            if remaining < 0 or i == len(coins):
                return 0

            take = dp(i, remaining - coins[i])
            skip = dp(i + 1, remaining)
            return take + skip

        return dp(0, amount)