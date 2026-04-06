# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid
        slow , fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow

        #reverse the second
        prev, curr =None, second

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        #merge first and second
        list1 , list2 = head, prev

        while list2.next:
            temp1, temp2 = list1.next, list2.next
            list1.next  = list2
            list2.next  = temp1
            list1,list2= temp1, temp2
            

