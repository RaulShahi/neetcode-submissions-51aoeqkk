class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(curr, sum_, i):
            if sum_ > target:
                return
            
            if sum_ == target:
                ans.append(curr[:])
                return 
            
            for j in range(i, n):
                curr.append(nums[j])
                sum_ += nums[j]
                backtrack(curr, sum_, j)
                curr.pop()
                sum_ -= nums[j]
        
        backtrack([], 0, 0)
        return ans
        