from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHouses(houses):
            if not houses:
                return 0
            if len(houses)==1:
                return houses[0]
            backTwo = houses[0]
            backOne = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                temp = backOne
                backOne = max(backTwo+houses[i], backOne)
                backTwo = temp
            return backOne
                
                

        return max(nums[0],robHouses(nums[:-1]), robHouses(nums[1:])) 
                
            


        