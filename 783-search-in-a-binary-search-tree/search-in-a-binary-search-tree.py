# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(curr,val):
            if curr and val < curr.val:
                if curr.left == None:
                    return None
                else:
                    curr = curr.left
                    return search(curr,val)
            elif curr and val > curr.val:
                if curr.right == None:
                    return None
                else:
                    curr = curr.right
                    return search(curr,val)
            elif curr:
                return curr
            else:
                return None
        return search(root,val)
            
        