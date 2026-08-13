# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        while head and head.val == val:
            head = head.next
        x = head
        while x and x.next:
            while x.next and x.next.val == val:
                x.next = x.next.next
            x = x.next
        return head
        

        