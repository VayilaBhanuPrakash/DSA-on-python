# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        prevgroup = dummy
        curr = prevgroup.next

        while True:
            kth = prevgroup
            for i in range(k):
                if kth:
                    kth = kth.next
            if not kth:
                break
            
            nextgroup = kth.next
            prev = nextgroup
            curr = prevgroup.next
            while curr != nextgroup:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            
            temp = prevgroup.next
            prevgroup.next = kth
            prevgroup = temp
        return dummy.next
        