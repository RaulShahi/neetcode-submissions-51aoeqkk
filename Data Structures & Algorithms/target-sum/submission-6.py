class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #bottom up approach
        total = sum(nums)
        if abs(target) > total:
            return 0
        n = len(nums)
        memo = [[0] * ((2*total)+1) for _ in range(n+1)]

        memo[n][target + total] = 1

        for i in range(n-1, -1, -1):
            for j in range((2*total)+1):
                curr_sum = j - total

                #subtract the element
                if curr_sum - nums[i] >= -total:
                    memo[i][j] += memo[i+1][curr_sum - nums[i]+total]
                if curr_sum + nums[i] <= total:
                    memo[i][j] += memo[i+1][curr_sum + nums[i]+total]

        return memo[0][total]