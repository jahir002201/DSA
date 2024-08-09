class PatriciaNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaNode("")

    def insert(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = PatriciaNode(char)
            node = node.children[char]

    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = PatriciaTrie()
trie.insert("hello")
print("Search 'hello':", trie.search("hello"))
print("Search 'world':", trie.search("world"))
