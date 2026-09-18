from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] = 1

        total = 0
        res = 0

        for num in nums:
            total += num
            diff = total - k

            res += prefixMap[diff]
            prefixMap[total] += 1
        
        return res

        