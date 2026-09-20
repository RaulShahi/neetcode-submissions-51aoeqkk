class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, curr):
            res.append(curr[:])
            if len(curr) == n:
                return
            
            for j in range(i, n):
                curr.append(nums[j])
                backtrack(j+1, curr)
                curr.pop()
        
        backtrack(0,[])
        return res

        