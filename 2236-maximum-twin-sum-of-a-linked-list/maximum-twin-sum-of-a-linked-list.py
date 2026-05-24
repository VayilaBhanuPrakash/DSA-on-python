# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev=ListNode(None)
        curr = second
        while curr != None:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        res = 0
        while head != None:
            twin = head.val + prev.val
            res = max(res,twin)
            head = head.next
            prev = prev.next
        return res

