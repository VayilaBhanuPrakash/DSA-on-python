# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        h = {}
        curr = head
        while curr:
            h[curr.val] = h.get(curr.val, 0) + 1
            curr = curr.next
        
        l = []
        curr = head
        while curr:
            if h[curr.val] == 1:
                l.append(curr.val)
            curr = curr.next
        if not l:
            return None
        curr = head
        prev = None
        for i in range(len(l)):
            curr.val = l[i]
            prev = curr
            curr = curr.next
        prev.next = None
        return head
        