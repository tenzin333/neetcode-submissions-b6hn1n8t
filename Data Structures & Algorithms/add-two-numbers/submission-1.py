# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0)
        tail = dummy

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1+num2 + carry 
            num3 =  total % 10 
            carry = total // 10

            node = ListNode(num3)
            tail.next = node
            tail = tail.next

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        return dummy.next
  







