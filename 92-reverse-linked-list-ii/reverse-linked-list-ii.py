# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        prev = dummy
        for i in range(left):
            prev = slow
            slow = slow.next
        
        count = right - left + 1
        rev = None

        while count > 0:
            after = slow.next
            slow .next = rev
            rev = slow
            slow = after
            count -= 1
        temp = rev

        while temp and temp.next:
            temp = temp.next
        temp.next = slow

        prev.next = rev

        return dummy.next


        

        
        