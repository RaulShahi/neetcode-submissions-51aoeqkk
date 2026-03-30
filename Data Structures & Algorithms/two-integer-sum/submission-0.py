from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = defaultdict(int)

        for i, v in enumerate(nums):
            if v in mapper:
                return [mapper[v],i]
            
            mapper[target-v] = i
        

        