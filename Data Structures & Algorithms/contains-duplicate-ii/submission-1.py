from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        index_list = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in index_list and i-index_list[nums[i]] <=k:
                return True
            index_list[nums[i]] = i
        
        return False
        