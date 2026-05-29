from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        total = sum(nums)

        if total%2 != 0:
            return False
        
        target = total/2

        @lru_cache(None)
        def dp(i, curr):
            if curr == target:
                return True
            
            if curr > target or i == len(nums):
                return False
            
            take = dp(i+1, curr+nums[i])
            skip = dp(i+1, curr)

            return take or skip
        
        return dp(0,0)
