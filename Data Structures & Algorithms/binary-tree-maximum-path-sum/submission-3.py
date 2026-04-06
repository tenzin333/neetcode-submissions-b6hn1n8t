# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node) -> int:
            if not node:
                return 0
            
            leftMax = max(dfs(node.left),0)
            rightMax = max(dfs(node.right),0)

            curr_path_sum = node.val + leftMax + rightMax

            self.maxSum = max(curr_path_sum, self.maxSum)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return self.maxSum