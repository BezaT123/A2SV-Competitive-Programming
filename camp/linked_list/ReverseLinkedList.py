# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = deque()
        current = head
        while current:
            stack.appendleft(current.val)
            current = current.next
        # print(stack)
        
        temp = ListNode()
        result = temp
        while len(stack) != 0:
            val = stack.popleft()
            node = ListNode(val)
            temp.next = node
            temp = temp.next
            
        return result.next
    
#         if not head:
#             return None
#         result  = None
#         temp = None
#         self.recursiveReverseList(head,temp,result)
#         return result
    
#     def recursiveReverseList(self, node, head, result):
        
#         if node.next:
#             self.recursiveReverseList(node.next,head,result)
#             head.next = node
#             head = head.next
#             # return new_node.next
#         else:
#             head = node
#             result = head
