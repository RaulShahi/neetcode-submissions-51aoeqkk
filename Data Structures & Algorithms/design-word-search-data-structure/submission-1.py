class TrieNode:
    
    def __init__(self):
        self.data = None
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        node = self.root

        for i in range(len(word)):
            if word[i] == ".":
                for child_nodes in node.children.values():
                    if(self.dfs(child_nodes, word, i)):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            else:
                node = node.children[word[i]]
            
        return node.isEnd
    
    def dfs(self, node, word, i):
        
        for j in range(i+1, len(word)):
            if word[j] == ".":
                for child in node.children.values():
                    if self.dfs(child, word, j):
                        return True
                return False
            elif word[j] not in node.children:
                return False
            else:
                node = node.children[word[j]]
        return node.isEnd
            

        
