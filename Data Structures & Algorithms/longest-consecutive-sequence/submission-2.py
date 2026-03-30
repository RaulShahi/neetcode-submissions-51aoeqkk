class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()

        i = 0
        ans = 1
        temp = [nums[i]]
        while i < len(nums)-1:
            if nums[i+1] -nums[i] == 1:
                temp.append(nums[i+1])
            elif nums[i+1] - nums[i] > 1:
                ans = max(ans, len(temp))
                temp =[nums[i+1]]
            i += 1
        return max(ans, len(temp))

