import pymongo
from views import mydb
# {'_id': ObjectId('64d9d9bca17aaa061db725f8'), 'character': '%', 'end': 'NO','children':{}}
# {'_id': ObjectId('64d9d9bca17aaa061db725f8'), 'character': '%', 'end': 'NO', 'children': {'a': {'end': 'YES', 'children': {'p': {'end': 'NO', 'children': {'p': {'end': 'NO', 'children': {'l': {'end': 'NO', 'children': {'e': {'end': 'YES', 'children': {}}}}}}}}}}, 'w': {'end': 'YES', 'children': {'o': {'end': 'YES', 'children': {'r': {'end': 'YES', 'children': {'d': {'end': 'YES', 'children': {}}}}}}}}, 'b': {'end': 'NO', 'children': {'o': {'end': 'NO', 'children': {'r': {'end': 'NO', 'children': {'d': {'end': 'NO', 'children': {'e': {'end': 'NO', 'children': {'r': {'end': 'YES', 'children': {}}}}}}}}}}}}, 'v': {'end': 'NO', 'children': {'a': {'end': 'NO', 'children': {'l': {'end': 'NO', 'children': {'e': {'end': 'NO', 'children': {'n': {'end': 'NO', 'children': {'t': {'end': 'NO', 'children': {'i': {'end': 'NO', 'children': {'n': {'end': 'NO', 'children': {'e': {'end': 'YES', 'children': {}, 'productID': 'P4253'}}}}}}}}}}}}}, 't': {'end': 'NO', 'children': {'i': {'end': 'NO', 'children': {'c': {'end': 'NO', 'children': {'a': {'end': 'NO', 'children': {'n': {'end': 'YES', 'children': {}, 'productID': 'P3423'}}}}}}}}}}}, 'e': {'end': 'NO', 'children': {'n': {'end': 'NO', 'children': {'i': {'end': 'NO', 'children': {'c': {'end': 'NO', 'children': {'e': {'end': 'YES', 'children': {}, 'productID': 'P423'}}}}}}}}}}}}}
# [{'character': 's', 'is_end_of_word': 'YES', 'children': []}]

Trie = mydb['Search']


class Search:

    def insert(self, word, productID):
        node = Trie.find_one()
        word = word.lower()
        root = node
        for char in word:
            if char not in node["children"].keys():
                node["children"][char] = {"end": "NO", "children": {}}
            node = node["children"][char]
        node["end"] = "YES"
        node["productID"] = productID
        Trie.update_one({"character": "%"}, {"$set": {"children": root["children"]}})

    def dfs(self, node, current_word, words):
        if (node['end']=='YES'):
            words[current_word]=node['productID']
        children = node['children']
        for i in children.keys():
            current_word += i
            self.dfs(node['children'][i], current_word, words)
            current_word = current_word[:-1]
        return

    def search(self, word):
        node = Trie.find_one()
        for char in word:
            if char not in node["children"].keys():
                return "NO"
            node = node["children"][char]
        return node["end"]

    def starts_with(self, prefix):
        node = Trie.find_one()
        print(node)
        for char in prefix:
            if char not in node['children'].keys():
                return {}
            node = node["children"][char]
        words = {}
        self.dfs(node, prefix, words)
        return words




search = Search()
# search.insert('vatican','P3423')
# print(search.starts_with("v"))
node = Trie.find_one({"character": "%"})
# print(node['children'])
# print(search.search("word"))
