class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def genSubset(curr, i):
            ans.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                genSubset(curr, j+1)
                curr.pop()
        
        genSubset([],0)
        return ans

        #Time complexity - The loop runs from 0 to n in first round, 1 to n second, 2 to n and so on 
        #So roughly O(n**2)
        #Space complexity - 2**n for the output