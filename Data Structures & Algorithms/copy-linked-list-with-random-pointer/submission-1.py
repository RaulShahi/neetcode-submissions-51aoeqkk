"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        dummy = Node(-1, None)
        prev = dummy
        curr =head

        while curr:
            nextNode = Node(curr.val)
            oldToNew[curr] = nextNode
            prev.next = nextNode
            prev = nextNode
            curr = curr.next
        
        curr = head

        while curr:
            if curr.random:
                oldToNew[curr].random = oldToNew[curr.random]
            else:
                oldToNew[curr].random = None 
            curr = curr.next
        
        return dummy.next

        