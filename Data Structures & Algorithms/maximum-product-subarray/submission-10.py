class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, maxm = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], cur_max*nums[i], cur_min*nums[i])
            cur_min = min(nums[i], cur_max*nums[i], cur_min*nums[i])
            maxm = max(maxm, temp)
            cur_max = temp
        
        return maxm

        