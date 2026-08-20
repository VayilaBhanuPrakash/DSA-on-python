# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        val1 = float('-inf')
        def inorder(root):
            nonlocal res
            nonlocal val1
            if root == None:
                return
            inorder(root.left)
            if val1 >= root.val:
                res = False
            val1 = root.val
            inorder(root.right)
        inorder(root)
        return res
        