class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1
        
        cur_total = 0
        start = 0

        for i in range(len(gas)):
            cur_total += gas[i] - cost[i]
            if cur_total < 0:
                start = i+1
                cur_total = 0
        
        return start
        