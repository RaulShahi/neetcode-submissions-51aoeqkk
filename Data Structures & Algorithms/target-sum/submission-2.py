class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = {0:1} #1 way to make sum 0

        for num in nums:
            new_dp = defaultdict(int)

            for cur_sum, count in dp.items():
                new_dp[cur_sum+num] += count
                new_dp[cur_sum-num] += count
            
            dp = new_dp
        
        return dp[target]
        