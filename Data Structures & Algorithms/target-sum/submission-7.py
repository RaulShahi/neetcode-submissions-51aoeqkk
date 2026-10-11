from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = {0:1}

        for num in nums:
            next_ways = defaultdict(int)
            for curr_sum , count in ways.items():
                next_ways[curr_sum+num] += count
                next_ways[curr_sum-num] += count
            
            ways = next_ways
        
        return ways.get(target, 0)


        