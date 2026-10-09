class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = [[-1] * (capacity+1) for _ in range(n)]
        def dfs_helper(i, capacity, memo):
            if i == len(profit):
                return 0
            
            if memo[i][capacity] != -1:
                return memo[i][capacity] 
            
            #skip
            memo[i][capacity] = dfs_helper(i+1, capacity, memo)

            #take
            new_capacity = capacity - weight[i]
            if new_capacity >= 0:
                p = profit[i] + dfs_helper(i+1, new_capacity, memo)
                memo[i][capacity] = max(memo[i][capacity], p)
        
            return memo[i][capacity]
        return dfs_helper(0, capacity, memo)