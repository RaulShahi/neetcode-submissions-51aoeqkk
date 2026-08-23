class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res = nums[0]

        def simpleSubarraySum(nums_temp):
            maxSum = nums_temp[0]
            curSum = 0

            for num in nums_temp:
                curSum = max(curSum, 0) + num
                maxSum = max(maxSum, curSum)
            
            return maxSum

        for i in range(len(nums)):
            nums_temp = nums[i:]
            if i > 0:
                nums_temp = nums[i:] + nums[0:i]            
            res = max(res, simpleSubarraySum(nums_temp))
        
        return res