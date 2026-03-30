class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = set(("+","-","/","*"))

        stack = []

        for c in tokens:
            if c not in symbols:
                stack.append(int(c))
            
            else:
                last, second_last = stack.pop(), stack.pop()

                if c == "+":
                    stack.append(last+second_last)
                
                elif c == "-":
                    stack.append(second_last-last)
                
                elif c == "*":
                    stack.append(last*second_last)
                elif c=="/":
                    stack.append(int(second_last/last))
        
        return stack[-1]
            
        