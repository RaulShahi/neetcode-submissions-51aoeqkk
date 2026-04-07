# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = head= ListNode(0)

        while l1 or l2:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            
            if l2:
                val += l2.val
                l2 = l2.next
            
            carry = int(val/10)

            curr.next = ListNode(val%10)
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return head.next
        



        