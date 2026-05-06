# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        dummy=ListNode(0)
        dummy.next=head
        res=dummy
        while dummy and dummy.next:
            if dummy.next.val in s:
                dummy.next=dummy.next.next
            else:
                dummy=dummy.next
        return res.next
        


        """s=set(nums)
        while head.val in s:
            head=head.next
        slow=head
        fast=head.next
        while fast and fast.next:
            if fast.val in s:
                slow.next=fast.next
                fast=fast.next
            else:
                slow=fast
                fast=slow.next
        if fast and fast.val in s:
            slow.next=None
        return head"""
        