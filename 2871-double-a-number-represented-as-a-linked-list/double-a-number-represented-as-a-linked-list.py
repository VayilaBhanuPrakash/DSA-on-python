# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0:
            return head
        n = 0
        x = head
        while x:
            n = n * 10 + x.val
            x = x.next
        res = n * 2
        x = head
        l =[]
        while res:
            rem = res % 10
            res =res //10
            l.append(rem)
        x = head
        i = len(l)-1
        while x:
            x.val = l[i]
            x = x.next
            i-=1
        x = head
        if i == 0:
            while x.next:
                x = x.next
            x.next = ListNode(l[0])
        return head