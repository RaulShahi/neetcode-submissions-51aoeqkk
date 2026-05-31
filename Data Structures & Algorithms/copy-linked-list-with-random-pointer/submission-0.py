"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1, None, None)
        prev = dummy

        curr = head
        mapper = {}
        while curr:
            nextNode = Node(curr.val)
            prev.next = nextNode
            mapper[curr] = nextNode
            curr = curr.next
            prev = nextNode
        
        curr = head
        while curr:
            if curr.random:
                mapper[curr].random = mapper[curr.random]
            else:
                mapper[curr].random = None
            curr = curr.next
        
        return dummy.next
        