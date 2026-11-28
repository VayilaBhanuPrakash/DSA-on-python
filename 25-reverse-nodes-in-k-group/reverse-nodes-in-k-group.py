# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        
        def reverse(i,j):
            while i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        
        for j in range(k - 1, len(l),k):
            reverse(j - k + 1, j)
        
        curr = head
        i = 0
        while curr:
            curr.val = l[i]
            i += 1
            curr = curr.next
        
        return head
        