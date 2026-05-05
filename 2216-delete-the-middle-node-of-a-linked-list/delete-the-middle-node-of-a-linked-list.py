# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head!=None and head.next==None:
            return None
        if head!=None and head.next!=None and head.next.next==None:
            head.next=None
            return head
        slow=ListNode(0)
        slow.next=head
        fast=head
        while fast and fast.next:
            slow =slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
        