class TrieNode:
    def __init__(self):
        self.data = None
        self.word = None
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for word in words:
            tree.insert(word)
        
        res = []

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m, n = len(board), len(board[0])

        visited = set()

        def isValid(r,c):
            return 0<=r<m and 0<=c<n and (r,c) not in visited 
        

        def dfs(r,c, node):
            if board[r][c] not in node.children:
                return 
            
            node = node.children[board[r][c]]
            if node.word:
                res.append(node.word)
            node.word = None

            for dx, dy in directions:
                nr, nc = r + dx, c + dy 
                if isValid(nr,nc):
                    visited.add((nr,nc))
                    dfs(nr,nc,node)
                    visited.remove((nr,nc))


        for i in range(m):
            for j in range(n):
                visited.add((i,j))
                dfs(i,j, tree.root)
                visited.remove((i,j))
        
        return res
        