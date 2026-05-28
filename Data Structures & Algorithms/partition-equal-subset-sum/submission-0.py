from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            #if total is odd, can't be partitioned into 2 parts
            return False

        target = total/2

        @lru_cache(None)
        def dp(i, summ):
            if summ == target:
                return True
            
            if summ > target or i==len(nums):
                return False
            
            take = dp(i+1, summ+nums[i])
            skip = dp(i+1, summ)

            return take or skip
        
        return dp(0,0)
        
 