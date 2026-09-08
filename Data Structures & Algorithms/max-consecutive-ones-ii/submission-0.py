class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numZeros = 0
        ans = 0
        L = 0
        
        for R, num in enumerate(nums):
            if num == 0:
                numZeros += 1
            
            while numZeros > 1:
                if nums[L] == 0:
                    numZeros -= 1
                L += 1
            
            ans = max(ans, R-L+1)
        
        return ans