from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum %2 == 1:
            return False
        
        target_sum = total_sum / 2
        memo = defaultdict(bool)

        def dfs(curr_sum, i):
            if curr_sum == target_sum:
                return True

            if curr_sum > target_sum:
                return False
            
            if i == len(nums):
                return False

            if (curr_sum, i) not in memo:

                #skip the item
                skip = dfs(curr_sum , i+1)

                # take the item
                take = dfs(curr_sum + nums[i], i+1)

                memo[(curr_sum, i)] = skip or take

            return memo[(curr_sum, i)]
        
        return dfs(0,0)