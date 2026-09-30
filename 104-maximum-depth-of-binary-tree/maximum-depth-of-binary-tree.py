# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None :
            return 0
        res = 0
        def dfs(root,height):
            nonlocal res
            if root == None:
                return 
            dfs(root.left,height+1)
            dfs(root.right,height+1)
            res = max(res,height)
        dfs(root,1)
        return res

        