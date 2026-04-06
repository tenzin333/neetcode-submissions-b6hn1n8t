# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def getHeight(node) -> int:
            if not node:
                return 0
            
            rightHeight = getHeight(node.right)
            leftHeight = getHeight(node.left)

            curr_height  = leftHeight + rightHeight
            self.max_diameter = max(curr_height,self.max_diameter)
            return 1 + max(leftHeight, rightHeight)
        
        getHeight(root)
        return self.max_diameter

