from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] = 1

        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixMap[diff]
            prefixMap[curSum] += 1
        
        return res
        
        
