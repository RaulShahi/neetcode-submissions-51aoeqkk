class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        ans = [0] * n
        for i in range(n-1,-1,-1):
            sum_ = digits[i] + carry
            carry = sum_ // 10
            ans[i]=sum_%10
        
        if carry:
            ans.insert(0, carry)
        
        return ans


