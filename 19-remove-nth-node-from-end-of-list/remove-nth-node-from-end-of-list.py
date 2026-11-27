# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        curr = head
        lenn = 0
        while curr:
            curr = curr.next
            lenn += 1
        
        remove = lenn - n
        curr = head
        if remove == 0:
            return head.next
        for i in range(1, remove):
            curr = curr.next
        curr.next = curr.next.next
        return head

        
        
        