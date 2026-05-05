# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        l=[]
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        curr=head
        for i in range(0,len(l),2):
            curr.val=l[i]
            curr=curr.next
        for i in range(1,len(l),2):
            curr.val=l[i]
            curr=curr.next
        return head





        