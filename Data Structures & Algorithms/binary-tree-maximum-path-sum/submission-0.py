# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(root)-> int:
            if not root:
                return 0
            
            leftmax = max(dfs(root.left),0)
            rightmax = max(dfs(root.right),0)
            curr_max = root.val + leftmax+ rightmax

            self.maxSum = max(curr_max,self.maxSum)
            return root.val + max(leftmax, rightmax)

        dfs(root)
        return self.maxSum