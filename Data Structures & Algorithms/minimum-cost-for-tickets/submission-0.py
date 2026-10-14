from collections import defaultdict
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = defaultdict(int)

        def dfs(i):
            if i == len(days):
                return 0
            
            if i not in memo:
                memo[i] = float("inf")
                j = i
                for cost, duration in zip(costs, [1,7,30]):
                    while j < len(days) and days[j] < days[i] + duration:
                        j += 1
                    memo[i] = min(memo[i], cost+dfs(j))
            return memo[i]
        return dfs(0)