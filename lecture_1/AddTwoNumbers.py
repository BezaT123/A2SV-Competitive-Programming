# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = result = ListNode(0)
        
        while l1 != None or l2 != None or carry != 0:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
                
            sum=l1.val+l2.val+carry
            carry=sum // 10
            sum =sum % 10
            result.next = ListNode(sum)
            l1=l1.next
            l2=l2.next
            result = result.next  
        return head.next