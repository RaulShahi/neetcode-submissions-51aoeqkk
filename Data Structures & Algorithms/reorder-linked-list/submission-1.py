# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            nN = second.next
            second.next = prev
            prev = second
            second = nN
        
        first , sec = head, prev

        while sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1
            first = tmp1
            sec = tmp2
            
        
        