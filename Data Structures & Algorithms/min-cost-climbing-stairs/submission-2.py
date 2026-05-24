class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        backOne = 0
        backTwo = 0

        for i in range(2, len(cost)+1):
            temp = min(backOne + cost[i-1], backTwo+cost[i-2])
            backTwo = backOne
            backOne = temp
        return backOne
        