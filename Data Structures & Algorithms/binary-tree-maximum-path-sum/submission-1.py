# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_sum_at_node = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.max_sum_at_node = max(self.max_sum_at_node, max(0, left)+max(0,right)+node.val)

            return node.val + max(0, max(left,right))
        
        dfs(root)

        return self.max_sum_at_node
        