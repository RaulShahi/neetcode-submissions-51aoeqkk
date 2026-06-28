from collections import defaultdict

class Node:
    def __init__(self, key,val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = defaultdict(dict)
        self.key_set = set() 
        
        #Initialize two dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        #connect them
        self.left.next = self.right
        self.right.prev = self.left
    
    #remove node from the linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    #insert node from the right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
        
