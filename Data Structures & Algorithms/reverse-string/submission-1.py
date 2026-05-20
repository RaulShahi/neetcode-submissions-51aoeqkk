class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #using recursion

        def helper(l, r, ls):
            if l >= r:
                return 
            ls[l], ls[r] = ls[r], ls[l]
            helper(l+1, r-1, ls)
        
        return helper(0, len(s)-1, s)
        