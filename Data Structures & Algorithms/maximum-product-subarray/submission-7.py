class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res , curMin, curMax = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp = max(num, curMax * num, curMin * num)
            curMin = min(num,curMax * num, curMin * num)
            curMax = temp

            res = max(res, curMax)

        return res
        