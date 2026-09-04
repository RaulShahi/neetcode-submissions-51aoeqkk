class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        INF = float("inf")
        ans = INF

        L = 0
        curr = 0
        for R in range(len(nums)):
            curr += nums[R]

            while curr >= target:
                ans = min(ans, R-L+1)
                curr -= nums[L]
                L += 1
        
        return 0 if ans == INF else ans



        