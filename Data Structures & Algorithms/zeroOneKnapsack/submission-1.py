class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        #using caching
        N,M = len(profit), capacity
        memo = [[-1] * (M+1) for _ in range(N)]

        def dfs_helper(i, capacity, memo):
            if i == N:
                return 0
            
            if memo[i][capacity] != -1:
                return memo[i][capacity]
            
            #skip the item
            memo[i][capacity] = dfs_helper(i+1, capacity, memo)

            #take the item
            new_capacity = capacity - weight[i]

            if new_capacity >= 0:
                memo[i][capacity] = max(memo[i][capacity], profit[i] + dfs_helper(i+1, new_capacity, memo))
            
            return memo[i][capacity]


        return dfs_helper(0, capacity, memo)