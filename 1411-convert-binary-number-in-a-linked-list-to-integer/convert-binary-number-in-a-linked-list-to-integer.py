# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res=0
        l=[]
        curr=head
        i=0
        while head:
            l.append(head.val)
            head=head.next
            i+=1
        i-=1
        for ele in l:
            if ele==1:
                res+=2**i
            i-=1
        return res
        
        