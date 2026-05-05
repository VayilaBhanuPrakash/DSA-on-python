# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

        
        """curr=head
        n=0
        while curr!=None:
            curr=curr.next
            n+=1
        n=n//2+1
        count=1
        curr=head
        while n!=count:
            head=head.next
            count+=1
        return head"""
        