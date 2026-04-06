# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1 . root > left and root > rigt , check left
# 2. root < left and root < right , check right
# 3. return root incase of split

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root,p,q)
    def dfs(self,node,p,q)-> TreeNode:
        if not node:
            return None
        
        if node.val > p.val and node.val > q.val:
            return self.dfs(node.left,p,q)
        elif node.val < p.val and node.val < q.val:
            return self.dfs(node.right,p,q)
        return node
    