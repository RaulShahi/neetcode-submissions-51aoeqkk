class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if ch in mapper:
                    stack.append(ch)
                else:
                    item = stack.pop()
                    if item not in mapper or mapper[item] != ch:
                        return False
        
        return len(stack) == 0
