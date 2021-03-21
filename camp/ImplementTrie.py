class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                node = Node()
                current.children[i] = node
            current = node
        current.endOfWord = True

    def search(self, word: str) -> bool:
        
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        
        if current.endOfWord:
            return True
        return False
            
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for i in prefix:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        return True

class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
