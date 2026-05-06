# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res=0
        curr=head
        i=0
        while head:
            head=head.next
            i+=1
        i-=1
        while curr:
            if curr.val==1:
                res+=2**i
            i-=1
            curr=curr.next
        return res
        
        