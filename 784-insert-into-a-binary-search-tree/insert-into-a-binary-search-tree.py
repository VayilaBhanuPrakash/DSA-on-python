# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(curr,val):
            r = curr
            if val < curr.val:
                if curr.left == None:
                    curr.left = TreeNode(val)
                else:
                    insert(curr.left,val)
            else:
                if curr.right == None:
                    curr.right = TreeNode(val)
                else:
                    insert(curr.right,val)
            return r
        if root == None:
            return TreeNode(val)
        return insert(root,val)
                
            
        