# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1=[]
        l2=[]
        curr=head
        while curr:
            if curr.val<x:
                l1.append(curr.val)
            else:
                l2.append(curr.val)
            curr=curr.next
        curr=head
        for ele in l1:
            curr.val=ele
            curr=curr.next
        for ele in l2:
            curr.val=ele
            curr=curr.next
        return head
        
        