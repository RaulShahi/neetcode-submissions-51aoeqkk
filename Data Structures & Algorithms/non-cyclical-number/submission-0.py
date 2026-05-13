class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set({n})

        while n>1:
            summ = 0
            temp = n
            while temp:
                summ += (temp%10) ** 2
                temp //= 10
            if summ in seen:
                return False
            seen.add(summ)
            n = summ
        
        return True

        