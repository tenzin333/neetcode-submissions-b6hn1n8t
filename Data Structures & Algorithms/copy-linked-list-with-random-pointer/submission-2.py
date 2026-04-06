"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # map of node with val
        oldToCopy = {}   #  nextpointer : NewNode(val)

        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        # copy
        curr = head
        
        while curr:
            copy = oldToCopy.get(curr)
            copy.next = oldToCopy.get(curr.next)
            copy.random = oldToCopy.get(curr.random)
            curr = curr.next
        return oldToCopy[head]














