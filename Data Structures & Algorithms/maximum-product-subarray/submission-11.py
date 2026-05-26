class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, maxm, minm = nums[0], nums[0], nums[0]

        for i in range(1,len(nums)):
            temp = max(maxm*nums[i], minm*nums[i], nums[i])
            minm = min(maxm*nums[i], minm*nums[i], nums[i])
            maxm = temp
            curr_max = max(curr_max, maxm)
        
        return curr_max

        