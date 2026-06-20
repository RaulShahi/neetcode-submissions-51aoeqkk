from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_list = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in index_list:
                for index in index_list[nums[i]]:
                    if abs(i-index) <= k:
                        return True
            index_list[nums[i]].append(i)
        
        return False