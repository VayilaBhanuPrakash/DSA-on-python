# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        l=[]
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        l.sort()
        curr=head
        i=0
        while curr!=None:
            curr.val=l[i]
            curr=curr.next
            i+=1
        return head

        