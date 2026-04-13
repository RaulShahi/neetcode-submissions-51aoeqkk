# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        self.ans = 0

        def dfs(node, maxm):
            if not node:
                return 
            
            if node.val >= maxm:
                self.ans += 1
                maxm = node.val
            dfs(node.left,maxm)
            dfs(node.right, maxm)
        

        dfs(root, root.val)
        return self.ans
            

        