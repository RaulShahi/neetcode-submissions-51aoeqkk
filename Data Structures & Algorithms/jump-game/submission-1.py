class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_d = 0

        for i in range(len(nums)):
            if max_d < i:
                return False
            
            max_d = max(max_d,i+nums[i])
        
        return True
        