# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def leaf(node):
            nonlocal res
            if node == None:
                return
            leaf(node.left)
            if node.left and node.left.left == None and node.left.right == None:
                res += node.left.val
            leaf(node.right)
        leaf(root)
        return res

        