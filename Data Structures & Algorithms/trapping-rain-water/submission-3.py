class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left, right = 0, n-1
        maxLeft, maxRight= height[left],height[right]
        ans = 0

        while left < right:
            if maxLeft < maxRight:
                ans += max(0, maxLeft - height[left])
                left += 1
                maxLeft = max(maxLeft, height[left])

            else:
                ans += max(0, maxRight - height[right])
                right -= 1
                maxRight = max(maxRight, height[right])
        
        return ans
            
            
        