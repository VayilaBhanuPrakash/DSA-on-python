# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        

        dummy = ListNode(0)
        dummy.next = head
        count = 0
        curr = head
        prev = dummy
        while count < left - 1:
            prev = curr
            curr = curr.next
            count += 1

        rev = None
        temp = curr
        while count < right:
            after = temp.next
            temp.next = rev
            rev = temp
            temp = after
            count += 1
    
        second_half = rev
        while rev.next:
            rev = rev.next

        rev.next = temp
        prev.next = second_half
        
        return dummy.next
        