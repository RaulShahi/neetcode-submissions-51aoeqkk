from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        n = len(nums)
        def dfs_helper(i, curr_sum):
            if i == n and curr_sum == target:
                return 1
            
            if i >= n:
                return 0
            
            if (i, curr_sum) not in memo:
                # add the item
                add = dfs_helper(i+1, curr_sum + nums[i])

                # sub the item
                sub = dfs_helper(i+1, curr_sum - nums[i])

                memo[(i, curr_sum)] = add + sub
            
            return memo[(i, curr_sum)]
        
        return dfs_helper(0, 0)
        