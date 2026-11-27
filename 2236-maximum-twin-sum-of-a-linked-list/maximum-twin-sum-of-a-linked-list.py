# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            after = slow.next
            slow.next = prev
            prev = slow
            slow = after
        res = 0
        while prev:
            summ = prev.val + head.val
            res = max(res,summ)
            prev = prev.next
            head = head.next
        return res

