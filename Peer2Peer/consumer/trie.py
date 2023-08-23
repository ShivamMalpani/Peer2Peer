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

    def dfs(self, node, current_word, words, productIDs):
        if (node['end']=='YES'):
            words.append(current_word)
        # print(node['end'])
        children = node['children']
        for key in children:
            # print(children[key])
            # if children[key]['end'] == "YES":
            #     words.append(current_word)
                # productIDs.append(node['productIDs'])
            for i in children.keys():
                current_word += i
                self.dfs(node['children'][i], current_word, words,productIDs)
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
        for char in prefix:
            if char not in node['children'].keys():
                return {}
            node = node["children"][char]
        words = []
        productIDs = []
        print(node)
        self.dfs(node, prefix, words, productIDs)
        return words, productIDs




search = Search()
print(search.starts_with(""))
node = Trie.find_one({"character": "%"})
# print(node['children'])
# print(search.search("word"))
