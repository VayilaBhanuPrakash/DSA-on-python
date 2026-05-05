# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a=[] 
        while head!=None:
            if head.val!=val:
                a.append(head.val)
            head=head.next
        root=None
        for ele in a:
            temp=ListNode(ele)
            if root==None:
                root=temp
                head=temp
            else:
                root.next=temp
                root=root.next
        return head


        """if head==None:
            return head
        curr=head
        while curr and curr.val==val:
            curr=curr.next
        head=curr
        while curr!=None and curr.next!=None:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head"""

        