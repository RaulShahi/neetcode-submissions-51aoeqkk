from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache
        def dp(summ, i): 
            if i > n-1:
                return 1 if summ == target else 0
            
            return dp(summ+nums[i] , i+1) + dp(summ-nums[i], i+1)
        
        return dp(0, 0)



    
        