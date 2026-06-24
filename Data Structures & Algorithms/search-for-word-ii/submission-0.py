class TrieNode:
    def __init__(self):
        self.data = None
        self.children = {}
        self.isEnd = False
    
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.isEnd = True
    
    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node.isEnd 
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for word in words:
            tree.insert(word)
        print(tree)
        m, n = len(board), len(board[0])
        res, visit = set(), set()

        def isValid(r,c, node):
            return 0<=r<m and 0<=c<n and (r,c) not in visit and board[r][c] in node.children
        
        directions = [[0,1], [0,-1],[1,0],[-1,0]]

        def dfs(r,c,node,word):
            if not isValid(r,c,node):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                dfs(nr,nc, node, word)
            visit.remove((r,c))
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,tree.root, "")
        
        return list(res)

