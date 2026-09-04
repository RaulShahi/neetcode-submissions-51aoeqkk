class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = height[0]
        maxRight = height[n-1]

        ans = 0
        L = 0
        R = n-1

        while L < R:
            if maxLeft < maxRight:
                ans += max(0, maxLeft-height[L])
                L += 1
                maxLeft = max(maxLeft, height[L])
            
            else:
                ans += max(0, maxRight-height[R])
                R -= 1
                maxRight = max(maxRight, height[R])
        
        return ans


        