# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def subtree(root):
            nonlocal res
            def avg(node):
                summ = 0
                count = 0
                def inorder(node):
                    nonlocal summ
                    nonlocal count
                    if node == None:
                        return
                    inorder(node.left)
                    summ += node.val
                    count += 1
                    inorder(node.right)
                inorder(node)
                average = summ // count
                return average
                   
            if root == None:
                return
            subtree(root.left)
            if avg(root) == root.val:
                res += 1
            subtree(root.right)
        subtree(root)
        return res
        