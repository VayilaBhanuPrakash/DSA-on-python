# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h={}
        curr=head
        i=0
        while curr!=None:
            if curr not in h:
                h[curr]=i
                curr=curr.next
                i+=1
            else:
                for i in range(i):
                    head=head.next
                return head
        return None
        