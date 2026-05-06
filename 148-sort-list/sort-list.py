# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        l.sort()
        res=ListNode(0) 
        result=res
        for ele in l:
            res.next=ListNode(ele)
            res=res.next
        return result.next      