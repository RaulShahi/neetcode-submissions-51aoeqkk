class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        if n > 0:
            return x**n
        
        else:
            temp = x
            while n<=0:
                temp = temp/x
                n += 1
            
            return temp