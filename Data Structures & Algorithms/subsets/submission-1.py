class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack(curr, i):
            #base case-if i > len(nums), dont search more
            if i > len(nums):
                return
            ans.append(curr[:])
            
            for j in range(i, n):
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()
        ans = []
        backtrack([],0)
        return ans
        