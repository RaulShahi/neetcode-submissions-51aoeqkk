class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = set(nums)
        return len(collection) != len(nums)
        