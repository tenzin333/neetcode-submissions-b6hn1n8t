# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def get_height(node) -> int:
            if not node:
                return 0
            
            right_height = get_height(node.right)
            left_height = get_height(node.left)
            curr_dia = right_height + left_height
            self.maxDiameter = max(curr_dia,self.maxDiameter)
            return 1 + max(left_height, right_height)
        
        get_height(root)
        return self.maxDiameter            
