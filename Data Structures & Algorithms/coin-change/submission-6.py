from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = defaultdict(int)
        def dfs(i, total):
            if total == 0:
                return 0
            if total < 0 or i == n:
                return float("inf")
            
            if (i, total) not in memo:
                memo[(i, total)]=min(dfs(i+1, total),
                1 + dfs(i, total - coins[i]))

            return memo[(i, total)]
        
        ans = dfs(0, amount)

        return -1 if ans == float("inf") else ans