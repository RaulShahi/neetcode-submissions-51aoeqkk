class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxSum = nums[0]
        curMax = 0

        minSum = nums[0]
        curMin = 0

        total = 0
        for num in nums:
            total += num

            curMax = max(curMax, 0) + num
            maxSum = max(maxSum, curMax)

            curMin = min(curMin, 0) + num
            minSum = min(curMin, minSum)
        
        # if all elements are negative
        if maxSum < 0:
            return maxSum

        circular_sum = total - minSum

        return max(circular_sum, maxSum)