# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        n=1
        while curr.next:
            curr=curr.next
            n+=1
        k=k%n
        curr=head
        for i in range(k):
            prev=None
            curr=head
            while curr.next:
                prev=curr
                curr=curr.next
            prev.next=None
            curr.next=head
            head=curr
        return curr
        

        