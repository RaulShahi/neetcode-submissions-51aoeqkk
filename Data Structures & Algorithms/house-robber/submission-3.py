class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        backTwo = nums[0]

        if n == 2:
            return max(nums[0], nums[1])
        
        backOne = max(nums[0], nums[1])

        for i in range(2, n):
            temp = max(nums[i]+backTwo, backOne)
            backTwo = backOne
            backOne = temp
        
        return backOne
        