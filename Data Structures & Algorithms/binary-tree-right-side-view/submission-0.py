from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # If this is the LAST node in the current level loop,
                # it's the one visible from the right side.
                if i == level_size - 1:
                    result.append(node.val)
                
                # Still add both children to keep the BFS going correctly
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result