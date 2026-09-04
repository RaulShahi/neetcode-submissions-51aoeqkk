class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        L,R = 0, n-1
        ans = 0

        while L < R:
            ln = R - L
            wt = min(heights[L], heights[R])
            ans = max(ans, ln*wt)

            if heights[L] < heights[R]:
                L += 1
            
            else:
                R -= 1
        
        return ans