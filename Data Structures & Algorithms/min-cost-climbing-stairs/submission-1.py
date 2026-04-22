class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        backTwo = 0
        backOne = 0

        for i in range(2, len(cost)+1):
            temp = min(backTwo+cost[i-2], backOne+cost[i-1])
            backTwo = backOne
            backOne = temp
        
        return backOne
        