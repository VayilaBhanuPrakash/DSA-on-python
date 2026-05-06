# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        l=[]
        while curr:
            l.append(curr.val)
            curr=curr.next
        left-=1
        right-=1
        while left<right:
            l[left],l[right]=l[right],l[left]
            left+=1
            right-=1
        res=ListNode(0)
        result=res
        for ele in l:
            res.next=ListNode(ele)
            res=res.next
        return result.next
        