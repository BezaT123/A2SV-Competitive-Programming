class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create k window min heap
        self.min_heap = []
        self.k = k
        
        for i in range(len(nums)):
            if i == k:
                break
            heapq.heappush(self.min_heap, nums[i])
            
        for i in range(k, len(nums)):
            self.add(nums[i])
            

    def add(self, val: int) -> int:
        # add new value to the heap
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val >= self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
            
        # return top of min heap
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
