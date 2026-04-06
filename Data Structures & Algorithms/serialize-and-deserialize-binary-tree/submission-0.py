# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1#2#3#N#N#4#5# where # represents end of digits and N reprsetns null values
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
            res = []

            def dfs(node) -> None:
                if not node:
                    res.append("N")
                    return 
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return "#".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        splitted = data.split("#")  # 1 , 2 , 3 , N , N, 4 
        queue = deque(splitted)

        def convertToTree(queue)-> TreeNode:
            if  queue:
                val = queue.popleft()
    
                if val == 'N':
                    return None

                node = TreeNode(val)

                node.left = convertToTree(queue)
                node.right = convertToTree(queue)
            return node
        return convertToTree(queue)








