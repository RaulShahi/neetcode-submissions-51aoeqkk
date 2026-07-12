class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
    
        num1 = num1[::-1]
        num2 = num2[::-1]

        ans = 0

        for j in range(len(num2)):
            prod = 0
            for i in range(len(num1)):
                prod += ((int(num1[i])*int(num2[j])) * (10**i))
            
            ans += (prod * (10**j))
        
        return str(ans)


            


        