class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = set(("+","-","/","*"))

        def calc(a,b,s):
            if s == "+":
                return int(a) + int(b)
            elif s == "-":
                return int(a)-int(b)
            elif s == "/":
                return int(int(a)/int(b))
            elif s=="*":
                return int(a)*int(b)

        stack = []

        for c in tokens:
            if c in symbols:
                last, second_last = stack.pop(), stack.pop()
                stack.append(calc(second_last, last, c))
            else:
                stack.append(int(c))
        
        return stack[-1]
        