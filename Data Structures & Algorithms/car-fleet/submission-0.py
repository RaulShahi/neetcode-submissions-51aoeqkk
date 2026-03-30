class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0
        
        pairs = [[p,r] for p,r in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]: #Reverse sorted order
            time = (target-p)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        