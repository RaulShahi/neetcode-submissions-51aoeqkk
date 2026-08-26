class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        left = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                length = min(length, right-left+1)
                total -= nums[left]
                left += 1


        return 0 if length == float("inf") else length
        