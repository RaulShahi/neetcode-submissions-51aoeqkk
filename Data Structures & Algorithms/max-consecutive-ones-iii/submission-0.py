class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        numZeros = 0
        L = 0
        ans = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                numZeros += 1
            
            while numZeros > k:
                if nums[L] == 0:
                    numZeros -= 1
                L += 1
            
            ans = max(ans, R-L+1)
        
        
        return ans
        