# current_node = {"character": 'a', "is_end_of_word": False,
#                 "children": [{"character": 'b', "is_end_of_word": False, "children": []}]}


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # node = self.root
        node = Trie.find_one({"character": "%"})
        root = node
        if node is None:
            pass

        for char in word:
            if char not in node.children:
                node.children[char] = {"character": char, "is_end_of_word": False, "children": []}
            node = node.children[char]
        node.is_end_of_word = True
        Trie.update_one({"character": "%"}, {"$set": {"children": root.children}})

    def search(self, word):
        node = Trie.find_one({"character": "%"})
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = Trie.find_one({"character": "%"})
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: True
print(trie.search("ban"))  # Output: False
print(trie.starts_with("bana"))  # Output: True
