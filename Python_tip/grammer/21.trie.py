class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True
        
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '*' in node
    
    def is_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
        

trie = Trie()
words = ['and', 'ant', 'do', 'dad']
for word in words:
    trie.insert(word)
    
serach_words = ["do", 'gee', 'bat']
print([trie.search(word) for word in serach_words])