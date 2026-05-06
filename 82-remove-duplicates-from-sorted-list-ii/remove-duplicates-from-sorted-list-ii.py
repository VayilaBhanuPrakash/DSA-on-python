# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        dup=set()
        curr=head
        while curr:
            if curr.val in s:
                dup.add(curr.val)
            else:
                s.add(curr.val)
            curr=curr.next
        res=ListNode(0,head)
        result=res
        while res.next:
            if res.next.val in dup:
                res.next=res.next.next
            else:
                res=res.next
        return result.next