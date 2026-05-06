# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """l=[]
        curr=head
        j=0
        while head:
            l.append(head.val)
            head=head.next
            j+=1
        i=0
        j-=1
        while i<j:
            if l[i]!=l[j]:
                return False
            i+=1
            j-=1
        return True"""

        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        rev=None
        curr=slow
        while curr:
            after=curr.next
            curr.next=rev
            rev=curr
            curr=after
        left=head
        right=rev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
        


        
        