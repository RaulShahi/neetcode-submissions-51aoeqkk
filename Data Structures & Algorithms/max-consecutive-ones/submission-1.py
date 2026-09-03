class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0

        for num in nums:
            cnt = cnt + 1 if num == 1 else 0
            ans = max(ans, cnt)
        
        return ans
        

        