class Node:
    def __init__(self, val=0, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap, self.cache = capacity, {}
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(value, key)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            leftNode = self.left.next
            self.remove(leftNode)
            del self.cache[leftNode.key]
