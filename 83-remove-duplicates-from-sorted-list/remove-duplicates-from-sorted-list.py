# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr=head
        after=curr.next
        while after:
            if curr.val==after.val:
                curr.next=after.next
                after=after.next
            else:
                curr=after
                after=after.next
        return head

        