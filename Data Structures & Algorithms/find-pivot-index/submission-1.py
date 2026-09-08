class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i, num in enumerate(nums):
            rightsum = total - leftsum - nums[i]
            if rightsum == leftsum:
                return i
            leftsum += nums[i]
        
        return -1