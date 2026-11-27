# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        curr1 = headA
        curr2 = headB
        while curr1:
            curr1 = curr1.next
            lenA += 1
        while curr2:
            curr2 = curr2.next
            lenB += 1
        
        if lenA > lenB:
            while lenA != lenB:
                headA = headA.next
                lenA -= 1
        
        if lenA < lenB:
            while lenA != lenB:
                headB = headB.next
                lenB -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

        
        