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

class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        my_trie = Trie()
        for root in dictionary:
            my_trie.insert(root)
        
        result = ""
        word_list = sentence.split()
        for word in word_list:
            
            string = self.replaceWordsUtil(my_trie, word) + " "
            result += string
            
        # print(result)
        return result[:len(result)-1]
    
    def replaceWordsUtil(self, trie, word):
        current = trie.root
        string = ""
        for i in word:
            node = current.children.get(i)
            string += i
            if node == None:
                return word
            if node.endOfWord == True:
                return string
            current = node
            
        return string
