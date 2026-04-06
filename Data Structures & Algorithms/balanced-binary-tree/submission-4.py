# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def checkBalance(node)-> bool:
            if not node:
                return False
            
            right = checkBalance(node.right)
            left = checkBalance(node.left)

            if right==-1:
                return -1
            
            if left==-1:
                return -1
            
            if abs(left-right) > 1:
                return -1
            return 1+max(left,right)
        
        return checkBalance(root)!= -1
            

