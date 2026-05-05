# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        curr=head
        lenn=1
        while curr.next:
            curr=curr.next
            lenn+=1
        remove=lenn-n
        curr=head
        if remove==0:
            return head.next
        for i in range(remove-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
        