# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        val1 = float('-inf')
        def inorder(root):
            nonlocal val1
            if root == None:
                return True
            if inorder(root.left) == False:
                return False
            if val1 >= root.val:
                return False
            val1 = root.val
            return inorder(root.right)
        return inorder(root)
        