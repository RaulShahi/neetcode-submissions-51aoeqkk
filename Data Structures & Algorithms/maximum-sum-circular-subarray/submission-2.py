class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curMax = nums[0]
        curMin = nums[0]
        total = nums[0]
        maxSum = nums[0]
        minSum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            total += num
            curMax = max(curMax, 0) + num
            curMin = min(curMin, 0) + num

            maxSum = max(curMax, maxSum)
            minSum = min(curMin, minSum)
        
        if maxSum < 0:
            return maxSum
        
        edge_sum = total - minSum

        return max(maxSum, edge_sum) 