class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            # 문자가 없으면 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 해당 문자로 이동
            curr_node = curr_node.children[char]
        # 끝난 지점의 노드의 data에 문자열 표시
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        if curr_node.data is not None:
            return True