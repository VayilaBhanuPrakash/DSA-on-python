# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        temp = head
        while temp != None:
            l.append(temp)
            temp = temp.next
        temp = head
        for i in range(len(l)//2):
            after = temp.next
            temp.next = l.pop()
            temp = temp.next
            temp.next = after
            temp = temp.next
        temp.next = None
        
        


        