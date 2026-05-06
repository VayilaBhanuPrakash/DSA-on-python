# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
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
        return head
        
        """num=set(nums)
        dummy=ListNode(0,head)
        prev=dummy
        while prev.next!=None:
            if prev.next.val in num:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return dummy.next"""



        