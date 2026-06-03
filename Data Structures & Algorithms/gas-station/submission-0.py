class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            tank = 0

            j = i
            while True:
                tank += gas[j]
                if tank < cost[j]:
                    break
                
                tank -= cost[j]
                j = (j+1)%n

                if j==i:
                    print("hey")
                    return i
        
        return -1
        