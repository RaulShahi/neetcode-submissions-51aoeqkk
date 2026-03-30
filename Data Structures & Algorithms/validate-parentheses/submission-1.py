class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(":")", "{":"}", "[":"]"}
        stack = []

        for c in s:
            if stack:
                if c in map:
                    stack.append(c)
                else:
                    last = stack[-1]
                    if last not in map or map[last] != c:
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
        