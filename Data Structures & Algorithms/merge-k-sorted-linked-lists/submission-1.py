# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        prev = ListNode(-1)
        dummy = prev

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        while heap:
            val, i, node = heappop(heap)
            prev.next = node
            prev = prev.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
        