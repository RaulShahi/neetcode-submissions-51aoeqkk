class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(":")","[":"]","{":"}"}
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in map:
                    stack.append(c)
                else:
                    item = stack.pop()
                    if item not in map or map[item] != c:
                        return False

        return len(stack) == 0

        