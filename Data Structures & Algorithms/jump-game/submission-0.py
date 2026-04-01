class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_d = 0

        for i in range(len(nums)):
            #check if we can reach this index
            if max_d < i:
                return False
            
            max_d = max(max_d, i+nums[i])
        
        return True
        