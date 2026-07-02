from collections import defaultdict
class ListNode:
    def __init__(self, key,val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val
    
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = defaultdict(dict)
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
