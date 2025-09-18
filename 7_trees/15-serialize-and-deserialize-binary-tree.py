# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = []
        q = deque([root])
        while q:
            length = len(q)

            for _ in range(length):
                node = q.popleft()
                if node == "None":
                    res.append("None")
                    continue

                res.append(str(node.val))
                nodeLeft = node.left if node.left else "None"
                q.append(nodeLeft)
                nodeRight = node.right if node.right else "None"
                q.append(nodeRight)
                
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        data = data.split(",")

        root = TreeNode(int(data[0]))
        q = deque([root])
        i = 0
        while q:
            length = len(q)

            for _ in range(length):
                node = q.popleft()

                i += 1
                if data[i] != "None":
                    node.left = TreeNode(int(data[i]))
                    q.append(node.left)

                i += 1
                if data[i] != "None":
                    node.right = TreeNode(int(data[i]))
                    q.append(node.right)
        
        return root
