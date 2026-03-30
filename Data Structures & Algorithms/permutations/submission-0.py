class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    curr.append(num)
                    backtrack(curr)
                    seen.remove(num)
                    curr.pop()
        
            
        ans = []
        seen = set()
        backtrack([])
        return ans

        