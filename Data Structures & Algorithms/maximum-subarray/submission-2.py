class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(0, cur_sum) + nums[i]
            curr_max = max(curr_max, cur_sum)
        
        return curr_max


        