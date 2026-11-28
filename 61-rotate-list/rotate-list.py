# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head
        k = k % n
        curr = head

        jumps = n - k - 1

        for i in range(jumps):
            curr = curr.next
        newhead = curr.next
        curr.next = None
        return newhead
        
        

        