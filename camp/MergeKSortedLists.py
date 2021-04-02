# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode()
        curr = result
        # create a min heap and add each node of the lists with indexes
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap,(lists[i].val,i))
                
        while min_heap:
            # get the min heap and update that node's head
            min_node = heapq.heappop(min_heap)
            node = lists[min_node[1]]
            if result:
                result.next = lists[min_node[1]]
                result = result.next
            
            # if the node's head is None, don't insert
            if node.next:
                heapq.heappush(min_heap,(node.next.val, min_node[1]))
                lists[min_node[1]] = lists[min_node[1]].next

        return curr.next
        
