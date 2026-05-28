# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1=[]
        stack2=[]
        head1=l1
        head2=l2
        while head1 and head2:
            stack1.append(head1.val)
            stack2.append(head2.val)
            head1=head1.next
            head2=head2.next
        while head1:
            stack1.append(head1.val)
            head1=head1.next
        while head2:
            stack2.append(head2.val)
            head2=head2.next
        carry=0
        res=None
        while stack1 or stack2 or carry:
            num=(stack1.pop() if stack1 else 0)+(stack2.pop() if stack2 else 0)+carry
            carry=num//10
            add=ListNode(num%10)
            add.next=res
            res=add
        return res




        