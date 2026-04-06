# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,i,node))

        dummy = ListNode()
        curr = dummy 

        while len(heap):
            val, i , node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next
            
            nxt = node.next

            if nxt:
                heapq.heappush(heap,(nxt.val,i,nxt))
        
        return dummy.next
