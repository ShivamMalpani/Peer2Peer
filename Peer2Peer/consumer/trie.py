import pymongo

# {'_id': ObjectId('64d9c37ca17aaa061db725f6'), 'character': '%', 'is_end_of_word': 'NO', 'children': [{'character': 's', 'is_end_of_word': 'YES', 'children': []}]}
# [{'character': 's', 'is_end_of_word': 'YES', 'children': []}]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Peer2Peer"]
Trie = mydb['Search']


class Search:

    def insert1(self, word):
        node = Trie.find_one()
        word = word.lower()
        root = node
        for char in word:
            if char not in node["children"].keys():
                node["children"][char] = {"end": "NO", "children": {}}
            node = node["children"][char]
        node["end"] = "YES"
        Trie.update_one({"character": "%"}, {"$set": {"children": root["children"]}})

    def search(self, word):
        node = Trie.find_one()
        for char in word:
            if char not in node["children"].keys():
                return "NO"
            node = node["children"][char]
        return node["end"]

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return "NO"
            node = node.children[char]
        return "YES"


node = Trie.find_one({"character": "%"})
print(node)
print(node['children'])

search = Search()
# search.insert1("border")
# print(search.search("word"))

