# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        n=0
        curr=head
        while curr!=None:
            curr=curr.next
            n+=1
        k=k%n
        curr=head
        for i in range(k):
            curr=head
            prev=None
            while curr.next:
                prev=curr
                curr=curr.next
            prev.next=None
            curr.next=head
            head=curr
        return curr
        

        