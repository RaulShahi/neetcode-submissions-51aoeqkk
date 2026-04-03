class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        res = []
        n = len(digits)
        
        def backtrack(curr, i):
            if len(curr) == n:
                res.append("".join(curr[:]))
                return 
            
            for letter in map[digits[i]]:
                curr.append(letter)
                backtrack(curr, i+1)
                curr.pop()

        if digits:
            backtrack([],0)
        return res



