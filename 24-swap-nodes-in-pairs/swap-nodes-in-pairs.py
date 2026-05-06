# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        swapped=ListNode(0)
        res=swapped
        curr=head
        i=1
        flag1=0
        flag2=0
        while curr:
            if i%2==0:
                val1=ListNode(curr.val)
                flag1=1
            else:
                val2=ListNode(curr.val)
                flag2=1
            i+=1
            curr=curr.next
            if flag1 and flag2:
                res.next=val1
                res=res.next
                res.next=val2
                res=res.next
                flag1=0
                flag2=0
        if flag2:
            res.next=val2
            res=res.next
        return swapped.next


        