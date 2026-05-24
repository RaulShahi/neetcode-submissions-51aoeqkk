class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def houserobSimple(nums):
            n = len(nums)
 
            backTwo = nums[0]
            backOne = max(nums[0], nums[1])

            for i in range(2, n):
                temp = max(nums[i]+backTwo, backOne)
                backTwo = backOne
                backOne = temp
            
            return backOne
        
        return max(houserobSimple(nums[1:]), houserobSimple(nums[:-1]))
        